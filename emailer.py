import smtplib
from email.message import EmailMessage

def send_email(sender, recipient, password, body):
    msg = EmailMessage()
    msg["Subject"] = "Test"
    msg["From"] = sender
    msg["To"] = recipient
    msg.set_content(body)

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
        smtp.login(sender, password)
        smtp.send_message(msg)
