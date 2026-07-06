import os
import ssl
import smtplib
import requests
import mimetypes
from email.message import EmailMessage
from email.policy import SMTP

SMTP_USER= os.environ.get('GMAIL_USER') or "weishenwong80@gmail.com"
SMTP_PASSWORD= os.environ.get('GMAIL_APP_PASSWORD')
secure_context=ssl.create_default_context()

if not SMTP_PASSWORD:
    raise ValueError("GMAIL_APP_PASSWORD enviornment variable is missing!")

try:
    smtp_object=smtplib.SMTP('smtp.gmail.com',587)
    smtp_object.starttls(context=secure_context)
    smtp_object.login(SMTP_USER,SMTP_PASSWORD)
except requests.exceptions.Timeout:
    print("The server took too long to respond")
    smtp_object.quit()
except requests.exceptions.ConnectionError:
    print("Network issue. Try again later")
    smtp_object.quit()
except requests.exceptions.HTTPError:
    print("HTTP error has occured.")
    smtp_object.quit()
except ssl.SSLCertVerificationError:
    print("Invalid SSL Cert!")
else:

    msg=EmailMessage(policy=SMTP)
    msg['Subject']="Python sending emai :)"
    msg['From']="Wei Shen <weishenwong80@gmail.com>"
    msg['To']="weishenwong80@gmail.com"
    msg.set_content("This is a test email from python!")
    smtp_object.send_message(msg)
    smtp_object.quit()