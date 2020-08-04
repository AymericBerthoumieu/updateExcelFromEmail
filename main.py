from emailManager import inbox, send_email, format_mail
from excelDbManager import interact_db
from process import *
import getpass

# E-mail data
emailAddress = 'clan.automate@gmail.com'
password = getpass.getpass(prompt='Password: ', stream=None)
host_smtp = 'smtp.gmail.com'
host_imap = 'imap.gmail.com'
port = 587

# Excel data
private_db_path = 'C:/Users/aym3r/Documents/CLAN/Privee_maccro_auto.xlsm'
public_db_path = 'C:/Users/aym3r/Documents/CLAN/Publique_maccro_auto.xlsm'
backup_folder_path = 'C:/Users/aym3r/Documents/CLAN/Backups'

public_headers = ['id_base', 'id_personne', 'domaine_etude', 'pays_etude', 'etablissement', 'parcours_com',
                  'domaine_pro', 'metier', 'employeur', 'pays_pro', 'com']
private_headers = ['id_personne', 'nom', 'prenom', 'email', 'tel', 'linkedin', 'situation', 'promo']


def main(private_db_path, public_db_path, backup_folder_path, host_imap, emailAddress, password, public_headers,
         private_headers):
    # create backup
    interact_db.create_backup(private_db_path, backup_folder_path)
    interact_db.create_backup(public_db_path, backup_folder_path)

    # get unseen e-mails
    unseen_messages = inbox.get_inbox(host_imap, emailAddress, password)

    # process e-mails
    for message in unseen_messages:
        sender = get_sender(message['from'])
        try:
            primary_key = process_message(message, public_headers, private_headers, public_db_path, private_db_path)
            if primary_key == -1:
                text = format_mail.format_done(message)
            else:
                text = format_mail.format_done_and_id(message, primary_key)
            subject = 'Done with request'
        except Exception as e:
            print(e)
            text = format_mail.format_error_response(message, e)
            subject = 'Error'
        # Inform sender if done or error
        send_email.send_mail(host=host_smtp, port=port, username=emailAddress, password=password, text=text,
                             subject=subject, from_email='Automate Clan <automate.clan@gmail.com>', to_emails=[sender])
    return None


main(private_db_path, public_db_path, backup_folder_path, host_imap, emailAddress, password, public_headers,
     private_headers)
