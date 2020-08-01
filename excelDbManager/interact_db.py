import shutil
import datetime


def create_backup(source, destination):
    """
    :param source: path to the file to copy
    :param destination: path to the back up folder
    :return: create a backup of source in destination
    """
    now = datetime.datetime.now()
    date = now.strftime("%Y_%m_%d__%Hh%M")
    name, extention = get_name_from_path(source)
    destination = destination + "/" + name + "_" + date + "." + extention
    try:
        shutil.copy(source, destination)
        backup = True
    except:
        backup = False
    return backup


def get_name_from_path(path):
    sep = path.split(sep='/')
    name_with_extention = sep[len(sep) - 1]
    name, extention = name_with_extention.split(".")
    return name, extention
