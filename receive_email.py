import imaplib
import getpass
import email

M = imaplib.IMAP4_SSL('imap.gmail.com')

#input email and password
#email=getpass.getpass('Email: ')
#password=getpass.getpass('Password: ')

M.login('weishenwong80@Gmail.com','kvow sfaw zrhn qxxw')
M.select('INBOX')
typ, data=M.search(None,'SUBJECT "Python sending email"')
#returns an array of results based on SUBJECT. Can be more than 1
email_id=data[0] #referring to first index of the results returned
result, email_data=M.fetch(email_id,'(RFC822)') #fetching content of the email. It is a tuple.
raw_email=email_data[0][1]
raw_email_string=raw_email.decode('utf-8')
email_message=email.message_from_string(raw_email_string)
for part in email_message.walk():
    if part.get_content_type()=='text/plain':
        body=part.get_payload(decode=True)
        print(body)

