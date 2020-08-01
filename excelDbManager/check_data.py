from excelDbManager.errors import *
from excelDbManager.interact_db import exist_in_db_id


def check_ajout_public(data, private):
    """
    :param data: dict containing the value of the cells to add a new line
    :param private : path to the private database
    :return: True if value are corrects else raise an exception
    """
    # id_base must be empty
    if 'id_base' in data:
        raise NonEmptyIdBaseError
    # id_personne must be filled
    if not ('id_personne' in data):
        raise EmptyIdPersonneError
    # id_personne must be an int
    try:
        data['id_personne'] = int(data['id_personne'])
    except:
        raise WrongIdPersonneTypeError
    # id_base must exist in excel file
    if not (exist_in_db_id(data['id_personne'], private)):
        raise UnknownIdPersonneError
    return True


def check_modif_public(data, public, private):
    """
    :param data: dict containing the value of the cells to change a line
    :param public : path to the public database
    :param private : path to the private database
    :return: True if value are corrects else raise an exception
    """
    # id_base must not be empty
    if not ('id_base' in data):
        raise EmptyIdBaseError
    # id_base must be an int
    try:
        data['id_base'] = int(data['id_base'])
    except:
        raise WrongIdBaseTypeError
    # id_base must exist in public file
    if not (exist_in_db_id(data['id_base'], public)):
        raise UnknownIdBaseError

    # id_personne must be filled
    if not ('id_personne' in data):
        raise EmptyIdPersonneError
    # id_personne must be an int
    try:
        data['id_personne'] = int(data['id_personne'])
    except:
        raise WrongIdPersonneTypeError
    # id_base must exist in excel file
    if not (exist_in_db_id(data['id_personne'], private)):
        raise UnknownIdPersonneError
    return True

