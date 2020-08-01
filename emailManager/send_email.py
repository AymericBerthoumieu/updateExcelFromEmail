from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from emailManager.connection_email import login_SMTP, logout_SMTP


def send(server, from_email: str = 'Automate Clan <automate.clan@gmail.com>', to_emails: list = [],
         msg_str: str = "Email body"):
    """
    :param server: smtp server
    :param from_email: e-mail address sending the message
    :param to_emails: list of e-mail address receiving the message
    :param msg_str: message as an str
    :return: send a msg_str from from_email to to_emails using server
    """
    try:
        server.sendmail(from_email, to_emails, msg_str)
        sent = True
    except:
        sent = False
    return sent


def create_message(text: str = 'Email Body', subject: str = 'Hello World',
                   from_email: str = 'Automate Clan <automate.clan@gmail.com>', to_emails: list = [None]):
    """
    :param text: e-mail body
    :param subject: e-mail subject
    :param from_email: e-mail sending message
    :param to_emails: e-mail receiving message
    :return: format email message
    """
    msg = MIMEMultipart('alternative')
    msg['From'] = from_email
    msg['To'] = ", ".join(to_emails)
    msg['Subject'] = subject
    txt_part = MIMEText(text, 'plain')
    msg.attach(txt_part)
    return msg.as_string()


def send_mail(host: str = 'smtp.gmail.com', port: int = 587, username: str = 'automate.clan@gmail.com',
              password: str = '', text: str = 'Email Body', subject: str = 'No Subject',
              from_email: str = 'Automate Clan <automate.clan@gmail.com>', to_emails: list = [None]):
    """
    :param host: smtp host
    :param port: smtp connection port
    :param username: e-mail address
    :param password: password of the e-mail address
    :param text: e-mail body
    :param subject: e-mail subject
    :param from_email: e-mail sending message
    :param to_emails: e-mail receiving message
    :return:
    """
    server = login_SMTP(host, port, username, password)
    message = create_message(text, subject, from_email, to_emails)
    sent = send(server, from_email, to_emails, message)
    logout = logout_SMTP(server)
    return sent, logout