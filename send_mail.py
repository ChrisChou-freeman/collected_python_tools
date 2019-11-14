from smtplib import SMTP_SSL
from email.mime.text import MIMEText
from email.header import Header
import getpass

class SendMail(object):
    def __init__(self, user_eamil, mail_title="test email", mail_content="test email"):
        self.host_server = 'smtp.qq.com' # choice your email smtp server
        self.pwd = ""
        self.sender_email = '1050434689@qq.com'
        self.receiver = user_eamil if user_eamil else self.sender_email
        self.mail_content = mail_content
        self.mail_title = mail_title

    def send(self):
        self.pwd = getpass.getpass("input your password>>")
        input("press anykey continue..")
        smtp = SMTP_SSL(self.host_server)
        smtp.set_debuglevel(1)
        smtp.ehlo(self.host_server)
        smtp.login(self.sender_email, self.pwd)
        
        msg = MIMEText(self.mail_content, "plain", 'utf-8')
        msg["Subject"] = Header(self.mail_title, 'utf-8')
        msg["From"] = self.sender_email
        msg["To"] = self.receiver
        smtp.sendmail(self.sender_email, self.receiver, msg.as_string())
        smtp.quit()

def main():
    try:
        title = input("email title>>")
        content = input("email content>>")
        s = SendMail('810676784@qq.com', mail_title=title, mail_content=content)
        s.send()
    except KeyboardInterrupt:
        exit()

if __name__ == "__main__":
    main()