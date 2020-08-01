from emailManager import inbox, send_email, format_mail
from excelDbManager import interact_db
from process import *

# E-mail data
emailAddress = 'clan.automate@gmail.com'
password = input('password :')
host_smtp = 'smtp.gmail.com'
host_imap = 'imap.gmail.com'
port = 587

# Excel data
private_db_path = ''
public_db_path = ''
backup_folder_path = ''

public_headers = ['id_base', 'id_personne', 'domaine_etude', 'pays_etude', 'parcours_com', 'domaine_pro', 'metier',
                  'employeur', 'pays_pro', 'com']
private_headers = ['id_personne', 'nom', 'prenom', 'email', 'tel', 'linkedin', 'situation', 'promo']


# send_email.send_mail(host_smtp, port, emailAddress, password, 'Email Body', 'No Subject', 'Automate Clan <automate.clan@gmail.com>', [emailAddress])

# unseen = inbox.get_inbox(host_imap, emailAddress, password)

def main(private_db_path, public_db_path, backup_folder_path, host_imap, emailAddress, password, public_headers, private_headers):
    # create backup
    interact_db.create_backup(private_db_path, backup_folder_path)
    interact_db.create_backup(public_db_path, backup_folder_path)

    # get unseen e-mails
    unseen_messages = inbox.get_inbox(host_imap, emailAddress, password)

    # process e-mails
    for message in unseen_messages:
        try:
            process_message(message, public_headers, private_headers, public_db_path, private_db_path)
        except Exception as e:
            sender = get_sender(message['from'])
            text = format_mail.format_error_response(message, e)
            send_email.send_mail(host=host_smtp, port=port, username=emailAddress, password=password, text=text,
                                 subject='Error', from_email='Automate Clan <automate.clan@gmail.com>',
                                 to_emails=[sender])

    return None
