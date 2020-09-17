from emailManager import inbox, send_email, format_mail
from excelDbManager import interact_db
from process import *
import getpass
import time

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

def backup(private_db_path, backup_folder_path, public_db_path):
    # create backup
    interact_db.create_backup(private_db_path, backup_folder_path)
    interact_db.create_backup(public_db_path, backup_folder_path)

def one_shot(private_db_path, public_db_path, backup_folder_path, host_imap, emailAddress, password, public_headers,
             private_headers, backup_indicator):
    # create backup
    if backup_indicator:
        backup(private_db_path, backup_folder_path, public_db_path)

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


def main(timelimit, private_db_path, public_db_path, backup_folder_path, host_imap, emailAddress, password,
         public_headers, private_headers, timeBackup):
    time1 = time.time()
    lastbackup = time.time()
    time2 = time.time()
    first_time = True
    while time2 - time1 < timelimit:
        backup_indicator = False
        if (time2 - lastbackup > timeBackup) or first_time: #on fait un backup des bases de données au premier passage et toutes les timeBackup
            backup_indicator = True
            first_time = False
        one_shot(private_db_path, public_db_path, backup_folder_path, host_imap, emailAddress, password, public_headers,
                 private_headers, backup_indicator)
        wait_minute(2)
        time2 = time.time()

timeBackup = 15*60
#main(3600*6, private_db_path, public_db_path, backup_folder_path, host_imap, emailAddress, password, public_headers,private_headers, timeBackup)

one_shot(private_db_path, public_db_path, backup_folder_path, host_imap, emailAddress, password, public_headers,
         private_headers, True)
