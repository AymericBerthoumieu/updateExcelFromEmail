import email
from emailManager.connection_email import login_IMAP4_SSL


def get_inbox(host: str = 'imap.gmail.com', username: str = 'automate.clan@gmail.com', password: str = ''):
    """
    :param host: imap host
    :param username: e-mail address
    :param password: password of the e-mail address
    :return: all unseen messages from inbox of username
    """
    mail = login_IMAP4_SSL(host=host, username=username, password=password)
    mail.select("inbox")
    _, search_data = mail.search(None, 'UNSEEN')
    my_message = []
    for num in search_data[0].split():
        my_message.append(get_message(mail, num))
    return my_message


def get_email_message(mail, num):
    """
    :param mail:
    :param num:
    :return:
    """
    _, data = mail.fetch(num, '(RFC822)')
    _, b = data[0]
    return email.message_from_bytes(b)


def get_email_body(part):
    """
    :param part:
    :return:
    """
    #
    if part.get_content_type() == 'multipart/alternative':
        body = part.get_payload()
        if isinstance(body,list):
            part = get_plain(body)

    # plain text
    if part.get_content_type() == "text/plain":
        key = 'body'
        body = part.get_payload(decode=True)
        body = body.decode()
    # html text
    elif part.get_content_type() == "text/html":
        key = 'html_body'
        html_body = part.get_payload(decode=True)
        body = html_body.decode()
    return key, body


def get_message(mail, num):
    """
    :param mail:
    :param num:
    :return:
    """
    email_data = {}
    _, data = mail.fetch(num, '(RFC822)')
    _, b = data[0]
    email_message = get_email_message(mail, num)
    # Get headers
    for header in ['subject', 'to', 'from', 'date']:
        email_data[header] = email_message[header]
    # Get e-mail body
    for part in email_message.walk():
        key, body = get_email_body(part)
        email_data[key] = body
    return email_data

def get_plain(messages):
    """
    :param messages: list of email.message.Message
    :return: message with content_type == 'text/plain'
    """
    i = 0
    while i < len(messages) and messages[i].get_content_type() != 'text/plain':
        i += 1
    if i >= len(messages):
        out = None
    else:
        out = messages[i]
    return out