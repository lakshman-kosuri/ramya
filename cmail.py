import smtplib
from email.message import EmailMessage
def sendmail(to,subject,body):
    server=smtplib.SMTP_SSL('smtp.gmail.com',465)
    server.login('kosurilakshman88@gmail.com','gejnyrvijxpadveb')
    msg=EmailMessage()
    msg['From']='kosurilakshman510@gmail.com'
    msg['To']=to
    msg['Subject']=subject
    msg.set_content(body)
    server.send_message(msg)
    server.quit()