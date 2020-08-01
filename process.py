from emailManager.errors import *


def process_message(message):
    # from gmail ?
    if not ('@gmail.com' in message['from']):
        raise GmailAddressesOnly
    # find action
    subject = message['Subject']
    if subject == '#Add #Public':
        pass
    elif subject == '#Add #Private':
        pass
    elif subject == '#Mod #Public':
        pass
    elif subject == '#Mod #Private':
        pass
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
