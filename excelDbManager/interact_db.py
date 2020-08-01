import shutil
import datetime
import openpyxl
import os, os.path
import win32com.client
from excelDbManager.errors import *

# Sheets
S_BASE = "Base"
S_MANAGE = "Manage"
S_MULTIPLE = "Ajouts Multiple"

# Cells
CELLS_PUBLIC = {'id_base': 'B2', 'id_personne': 'C2', 'domaine_etude': 'D2', 'pays_etude': 'E2', 'etablissement': 'F2',
                'parcours_com': 'G2', 'domaine_pro': 'H2', 'metier': 'I2', 'employeur': 'J2', 'pays_pro': 'K2',
                'com': 'L2'}
CELLS_PRIVATE = {'id_personne': 'B3', 'nom': 'C3', 'prenom': 'D3', 'email': 'E3', 'tel': 'F3', 'linkedin': 'G3',
                 'situation': 'H3', 'promo': 'I3'}


def create_backup(source, destination):
    """
    :param source: path to the file to copy
    :param destination: path to the back up folder
    :return: create a backup of source in destination
    """
    now = datetime.datetime.now()
    date = now.strftime("%Y_%m_%d__%Hh%M")
    name, extension = get_name_from_path(source)
    destination = destination + "/" + name + "_" + date + "." + extension
    try:
        shutil.copy(source, destination)
        backup = True
    except:
        backup = False
    return backup


def get_name_from_path(path):
    """
    :param path:
    :return: extract name and extension of
    """
    sep = path.split(sep='/')
    name_with_extension = sep[len(sep) - 1]
    name, extension = name_with_extension.split(".")
    return name, extension


def exist_in_db_id(id, source):
    """
    :param id: int
    :param source: path to database
    :return: True if id exist in source else False
    """
    wb = openpyxl.load_workbook(filename=source)
    sheet = wb[S_BASE]
    row = 3
    while (sheet['A' + str(row)].value is not None) and (sheet['A' + str(row)].value != id):
        row += 1
    if sheet['A' + str(row)].value is None:
        exist = False
    else:
        exist = True
    return exist


def run_maccro(excel_file, maccro_name):
    try:
        xl = win32com.client.Dispatch("Excel.Application")
        xl.Workbooks.Open(os.path.abspath(excel_file))
        xl.Application.Run(excel_file + "!Maccros." + maccro_name)
        xl.Application.Save()
        xl.Application.Quit()
        del xl
    except:
        raise MaccroError
    return True


def get_last_id_personne(path_to_private_db):
    wb = openpyxl.load_workbook(filename=path_to_private_db)
    sheet = wb[S_BASE]
    row = 1
    while sheet['A' + str(row)].value is not None:
        row += 1
    return sheet['A' + str(row - 1)].value


def add_line_public(data, path):
    wb = openpyxl.load_workbook(filename=path)
    sheet = wb[S_MANAGE]
    # Place data
    for key, value in data:
        sheet[CELLS_PUBLIC[key]].value = value
    # save to take change into account
    wb.save(path)
    # activate maccro
    run_maccro(path, 'Ajouter_ligne_python')
    return -1


def add_line_private(data, path):
    wb = openpyxl.load_workbook(filename=path)
    sheet = wb[S_MANAGE]
    # Place data
    for key, value in data:
        sheet[CELLS_PRIVATE[key]].value = value
    # save to take change into account
    wb.save(path)
    # activate maccro
    run_maccro(path, 'Ajouter_ligne_python')
    # Get last id personne to tell the requester
    id_personne = get_last_id_personne(path)
    return id_personne


def modif_line_public(data, path):
    wb = openpyxl.load_workbook(filename=path)
    sheet = wb[S_MANAGE]
    # Place data
    for key, value in data:
        sheet[CELLS_PUBLIC[key]].value = value
    # save to take change into account
    wb.save(path)
    # activate maccro
    run_maccro(path, 'Modifier_ligne_python')
    return -1


def modif_line_private(data, path):
    wb = openpyxl.load_workbook(filename=path)
    sheet = wb[S_MANAGE]
    # Place data
    for key, value in data:
        sheet[CELLS_PRIVATE[key]].value = value
    # save to take change into account
    wb.save(path)
    # activate maccro
    run_maccro(path, 'Modifier_ligne_python')
    return -1
