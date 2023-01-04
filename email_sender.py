import smtplib
from email.message import EmailMessage
from string import Template  # used for replacing the variable in HTML file
from pathlib import Path  # sim. to os, used for accessing the HTML file
# receives html file as string and template used for replacing the variables
html = Template(Path('index.html').read_text())
email = EmailMessage()  # creates EmailMessage object
email['from'] = 'Ritvik Mahapatra'
email['to'] = 'ritvik.mahapatra@yahoo.com'
email['subject'] = 'Test Mail!!'

# subs name, multiple variables can be used, second 'html' tells that the set_content is of HTML type
email.set_content(html.substitute({'name': 'Ritvik Mahapatra'}), 'html')

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:  # host as gmail, port is gen.587
    smtp.ehlo()  # intiates the protocol
    smtp.starttls()
    smtp.login('ritvikmahapatra777@gmail.com',
               'Tannushree2010')  # login credentials
    smtp.send_message(email)  # sends the mail
print('mail sent')
