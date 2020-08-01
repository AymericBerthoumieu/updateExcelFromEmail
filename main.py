from emailManager import inbox, send_email

# E-mail data
emailAddress = 'clan.automate@gmail.com'
password = 'ViveleCLAN47600!'
host_smtp = 'smtp.gmail.com'
host_imap = 'imap.gmail.com'
port = 587

# Excel data
private_db_path = ''
public_db_path = ''
backup_folder_path = ''


#send_email.send_mail(host_smtp, port, emailAddress, password, 'Email Body', 'No Subject', 'Automate Clan <automate.clan@gmail.com>', [emailAddress])

unseen = inbox.get_inbox(host_imap, emailAddress, password)

for message in unseen:
    print(message)
    print('\n \n')
    for j in message:
        print(j)

print(unseen[0]['body'])