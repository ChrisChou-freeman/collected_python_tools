# -*- coding: utf-8 -*-
from smtplib import SMTP_SSL
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header
import getpass
import sys


if sys.version_info[0]==2:
    input = raw_input
else:
    input = input

class SendMail(object):
    def __init__(self, user_eamil, mail_title="test email", mail_content="test email", file_path=""):
        self.host_server = 'smtp.qq.com' # your smtp email server
        self.pwd = ""
        self.sender_email = '1050434689@qq.com'
        self.receiver = user_eamil if user_eamil else self.sender_email
        self.mail_content = mail_content
        self.mail_title = mail_title
        self.file_path = file_path

    def send(self):
        self.pwd = getpass.getpass("input your password>>")
        input("press anykey continue..")
        smtp = SMTP_SSL(self.host_server)
        smtp.set_debuglevel(1)
        smtp.ehlo(self.host_server)
        smtp.login(self.sender_email, self.pwd)
        
        mail_text = MIMEText(self.mail_content, "plain", 'utf-8')
        msg = MIMEMultipart()
        msg["Subject"] = Header(self.mail_title, 'utf-8')
        msg["From"] = self.sender_email
        msg["To"] = self.receiver
        msg.attach(mail_text)

        try:
            with open(self.file_path, 'rb') as r:
                print("file reading...")
                content2 = MIMEText(r.read(), "base64", "utf-8")
                content2["Content-Type"] = 'application/octet-stream'
                content2["Content-Disposition"] = 'attachment; filename="the_file.{}"'.format(
                    self.file_path.rsplit('.', 1)[-1]
                )
                msg.attach(content2)
        except Exception:
            print("file reading error!!")
            exit()
        print("file reading success...")
        smtp.sendmail(self.sender_email, self.receiver, msg.as_string())
        smtp.quit()

def main():
    try:
        title = input("email title>>")
        content = input("email content>>")
        file_path = input("input your file_path>>")
        s = SendMail(
            '1050434689@qq.com',
            mail_title=title,
            mail_content=content,
            file_path=file_path
        )
        s.send()
    except KeyboardInterrupt:
        exit()

if __name__ == "__main__":
    main()