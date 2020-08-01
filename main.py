from emailManager import inbox, send_email
from excelDbManager import interact_db

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


#send_email.send_mail(host_smtp, port, emailAddress, password, 'Email Body', 'No Subject', 'Automate Clan <automate.clan@gmail.com>', [emailAddress])

#unseen = inbox.get_inbox(host_imap, emailAddress, password)

interact_db.create_backup('C:/Users/aym3r/Documents/CLAN/Publique_maccro.xlsm', 'C:/Users/aym3r/Documents/CLAN/')