from celery import Celery
import smtplib
import email
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
import time

app = Celery('test', broker='pyamqp://guest@localhost//')

'''
to start delery worker : celery -A test worker --loglevel=info
to start rabbitmq : first export path 
            export PATH=$PATH:/usr/local/sbin (or put into .bash_profile)
            cmd : rabbitmq-server
            url : http://localhost:15672/
            default user, pass : guest, guest
'''

@app.task
def send_email(subject, text_data = None, file_name = None):
    to_address = 'charu.matta@yahoo.com'
    body_mail_text =  text_data
    fromaddr = "charumatta1204@gmail.com"
    msg = MIMEMultipart()
    msg['From'] = fromaddr
    msg['To'] = to_address
    msg['Subject'] = subject
    if file_name:
            part = MIMEBase('application', "octet-stream")
            part.set_payload(open(file_name, "rb").read())
            # Encoders.encode_base64(part)
            part.add_header('Content-Disposition', 'attachment; filename="random.csv"')
            msg.attach(part)
            msg.attach(MIMEText("Hi,\n Please find the attach csv."))
    else:
        body = body_mail_text
        msg.attach(MIMEText(body, 'html'))
    text = msg.as_string()
    try:
        s_mail=smtplib.SMTP(host='smtp.gmail.com', port=587)
        s_mail.ehlo()
        s_mail.starttls()
        s_mail.ehlo()
        s_mail.login('charumatta1204@gmail.com', 'myonl9shop@12')
        s_mail.sendmail(fromaddr, to_address.split(','), text)
        return "done"
    except Exception as R:
        print("no send",R)
        return R

if __name__ == '__main__':
    send_email("Celery Test Mail",text_data = 'attachment', file_name ='/Users/chauabhi/Documents/Workspace/practice/random.csv')
    print ("End")

