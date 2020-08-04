import shutil
import datetime
import os
import os.path
import win32com.client
from excelDbManager.errors import *

xlOpenXMLWorkbookMacroEnabled = 52

# Sheets
S_BASE = "Base"
S_MANAGE = "Manage"
S_MULTIPLE = "Ajouts Multiple"

# Cells
CELLS_PUBLIC = {'id_base': 1, 'id_personne': 2, 'domaine_etude': 3, 'pays_etude': 4, 'etablissement': 5,
                'parcours_com': 6, 'domaine_pro': 7, 'metier': 8, 'employeur': 9, 'pays_pro': 10, 'com': 11, 'date': 12}
CELLS_PRIVATE = {'id_personne': 1, 'nom': 2, 'prenom': 3, 'email': 4, 'tel': 5, 'linkedin': 6, 'situation': 7,
                 'promo': 8, 'date': 9}


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


def get_first_empty_row(sheet):
    primary_key = -1
    row = 3
    while sheet.Cells(row, 1).value is not None:
        primary_key = max(primary_key, sheet.Cells(row, 1).value)
        row += 1
    return row, primary_key + 1


def exist_in_db_id(key, path):
    xl = win32com.client.Dispatch("Excel.Application")  # activate excel
    wb = xl.Workbooks.Open(os.path.abspath(path))  # open workbook
    xlSheet = wb.Sheets(S_BASE)  # select sheet
    try:
        get_line_by_id(key, xlSheet)
        exist = True
    except:
        exist = False
    return exist


def get_line_by_id(primary_key, sheet):
    row = 3
    while (sheet.Cells(row, 1).value != primary_key) and (sheet.Cells(row, 1).value is not None):
        row += 1
    if sheet.Cells(row, 1).value is None:
        raise IdUnknown(primary_key)
    return row


def add_line_public(data, path):
    xl = win32com.client.Dispatch("Excel.Application")  # activate excel
    wb = xl.Workbooks.Open(os.path.abspath(path))  # open workbook
    xlSheet = wb.Sheets(S_BASE)  # select sheet
    # find where to write
    row, primary_key = get_first_empty_row(xlSheet)

    # add data
    xlSheet.Cells(row, CELLS_PUBLIC['id_base']).value = primary_key
    xlSheet.Cells(row, CELLS_PUBLIC['date']).value = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    for element in data:
        if (element != 'id_base') and (element != 'date'):
            xlSheet.Cells(row, CELLS_PUBLIC[element]).value = data[element]

    # save and quit
    xl.DisplayAlerts = False  # avoid the alert about replacing the file
    wb.SaveAs(os.path.abspath(path), FileFormat=xlOpenXMLWorkbookMacroEnabled)  # save file with macros
    xl.Quit()
    return int(primary_key)


def add_line_private(data, path):
    xl = win32com.client.Dispatch("Excel.Application")  # activate excel
    wb = xl.Workbooks.Open(os.path.abspath(path))  # open workbook
    xlSheet = wb.Sheets(S_BASE)  # select sheet
    # find where to write
    row, primary_key = get_first_empty_row(xlSheet)

    # add data
    xlSheet.Cells(row, CELLS_PRIVATE['id_personne']).value = primary_key
    xlSheet.Cells(row, CELLS_PRIVATE['date']).value = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    for element in data:
        if (element != 'id_personne') and (element != 'date'):
            xlSheet.Cells(row, CELLS_PRIVATE[element]).value = data[element]

    # save and quit
    xl.DisplayAlerts = False  # avoid the alert about replacing the file
    wb.SaveAs(os.path.abspath(path), FileFormat=xlOpenXMLWorkbookMacroEnabled)  # save file with macros
    xl.Quit()
    return int(primary_key)


def modif_line_public(data, path):
    xl = win32com.client.Dispatch("Excel.Application")  # activate excel
    wb = xl.Workbooks.Open(os.path.abspath(path))  # open workbook
    xlSheet = wb.Sheets(S_BASE)  # select sheet
    # find where to write
    row = get_line_by_id(data['id_base'], xlSheet)

    # do modification
    xlSheet.Cells(row, CELLS_PUBLIC['date']).value = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    for element in data:
        if (element != 'id_base') and (element != 'date'):
            xlSheet.Cells(row, CELLS_PUBLIC[element]).value = data[element]

    # save and quit
    xl.DisplayAlerts = False  # avoid the alert about replacing the file
    wb.SaveAs(os.path.abspath(path), FileFormat=xlOpenXMLWorkbookMacroEnabled)  # save file with macros
    xl.Quit()
    return -1


def modif_line_private(data, path):
    xl = win32com.client.Dispatch("Excel.Application")  # activate excel
    wb = xl.Workbooks.Open(os.path.abspath(path))  # open workbook
    xlSheet = wb.Sheets(S_BASE)  # select sheet
    # find where to write
    row = get_line_by_id(data['id_personne'], xlSheet)

    # do modification
    xlSheet.Cells(row, CELLS_PUBLIC['date']).value = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    for element in data:
        if (element != 'id_personne') and (element != 'date'):
            xlSheet.Cells(row, CELLS_PRIVATE[element]).value = data[element]

    # save and quit
    xl.DisplayAlerts = False  # avoid the alert about replacing the file
    wb.SaveAs(os.path.abspath(path), FileFormat=xlOpenXMLWorkbookMacroEnabled)  # save file with macros
    xl.Quit()
    return -1
