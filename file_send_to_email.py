# -*- coding: utf-8 -*-
from smtplib import SMTP_SSL
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header
import sys
import json
import logging


if sys.version_info[0]==2:
    input = raw_input
else:
    input = input

class SendMail(object):
    def __init__(
        self,
        sender_mail,
        to_eamil,
        mail_title="test email",
        mail_content="test email",
        file_path="",
        pass_word=""
    ):
        self.host_server = 'smtp.qq.com' # your smtp email server
        self.pwd = pass_word
        self.sender_email = sender_mail
        self.receiver = to_eamil if to_eamil else self.sender_email
        self.mail_content = mail_content
        self.mail_title = mail_title
        self.file_path = file_path

    def send(self):
        smtp = SMTP_SSL(self.host_server)
        # smtp.set_debuglevel(1)
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
            sys.exit()
        print("file reading success...")
        smtp.sendmail(self.sender_email, self.receiver, msg.as_string())
        smtp.quit()

def main():
    '''
    //sender_conf.json
    {
        "your_email": "email",
        "passward": "",
        "send_to": "email",
        "title": "test",
        "content": "test",
        "file_path": "./1.txt"
    }
    '''
    r = open("./sender_conf.json", "r")
    data = r.read()
    data = json.loads(data)
    r.close()
    try:
        title = data["title"]
        content = data["content"]
        file_path = data["file_path"]
        your_email = data["your_email"]
        passward = data["passward"]
        to_email = data["send_to"]
        s = SendMail(
            your_email,
            to_email,
            mail_title=title,
            mail_content=content,
            file_path=file_path,
            pass_word=passward
        )
        s.send()
        print("mail sent success..")
    except KeyboardInterrupt:
        sys.exit()

if __name__ == "__main__":
    main()
    