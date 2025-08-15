import smtplib
from email.mime.text import MIMEText
from config import Config

def send_email(to, subject, body):
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = Config.MAIL_USERNAME
    msg['To'] = to
    
    with smtplib.SMTP(Config.MAIL_SERVER, Config.MAIL_PORT) as server:
        server.login(Config.MAIL_USERNAME, Config.MAIL_PASSWORD)
        server.send_message(msg)