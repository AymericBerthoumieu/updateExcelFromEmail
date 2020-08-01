import shutil
import datetime
import openpyxl

# Sheets
S_BASE = "Base"
S_MANAGE = "Manage"
S_MULTIPLE = "Ajouts Multiple"

# Cells
C_ID_BASE = "B3"
C_ID_PERSONNE = "C3"
C_END_LINE = "L3"
C_STATUS = "G9"

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
    sheet = wb['Base']
    row = 3
    while (sheet['A'+ str(row)].value is not None) and (sheet['A'+ str(row)].value != id):
        row += 1
    if sheet['A'+ str(row)].value is None:
        exist = False
    else:
        exist = True
    return exist