from emailManager.errors import *
from emailManager import format_mail
from excelDbManager import check_data, interact_db


def process_message(message, public_headers, private_headers, public_db_path, private_db_path):
    # from gmail ?
    if not ('@gmail.com' in message['from']):
        raise GmailAddressesOnly
    # find action
    subject = message['Subject']
    if subject == '#Add #Public':
        data = format_mail.format_data(message['body'], public_headers)
        check_data.check_add_public(data, private_db_path)
        interact_db.add_line(data, public_db_path)
    elif subject == '#Add #Private':
        data = format_mail.format_data(message['body'], private_headers)
        check_data.check_add_private(data)
        interact_db.add_line(data, private_db_path)
    elif subject == '#Mod #Public':
        data = format_mail.format_data(message['body'], public_headers)
        check_data.check_modif_public(data, public_db_path, private_db_path)
        interact_db.modif_line(data, public_db_path)
    elif subject == '#Mod #Private':
        data = format_mail.format_data(message['body'], private_headers)
        check_data.check_modif_private(data, private_db_path)
        interact_db.modif_line(data, public_db_path)
    else:
        raise UnunderstandableSubject


def get_sender(sender_str):
    """
    :param sender_str:
    :return: e-mail address of sender
    """
    if '<' in sender_str:
        sender_str = sender_str[sender_str.index('<') + 1:sender_str.index('>')]
    return sender_str
