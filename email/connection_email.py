import smtplib
import imaplib

def login_SMTP(host: str = 'smtp.gmail.com', port: int = 587, username: str = 'automate.clan@gmail.com', password: str = ''):
    """
    :param host:
    :param port:
    :param username: e-mail address
    :param password: password of the e-mail address
    :return: login to Gmail's smtp server
    """
    server = smtplib.SMTP(host=host, port=port)
    server.ehlo()
    server.starttls()
    server.login(username, password)
    return server


def logout_SMTP(server):
    """
    :param server: smtp server
    :return: logout from server
    """
    try:
        server.quit()
        out = True
    except:
        out = False
    return out

def login_IMAP4_SSL(host: str = 'imap.gmail.com', username: str = 'automate.clan@gmail.com', password: str = ''):
    mail = imaplib.IMAP4_SSL(host)
    mail.login(username, password)
    return mail
