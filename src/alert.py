import smtplib
from email.message import EmailMessage

def send_alert(transaction):
    msg = EmailMessage()
    msg.set_content(f"Fraud Alert: {transaction}")
    msg["Subject"] = "⚠️ Fraud Detected"
    msg["From"] = "you@example.com"
    msg["To"] = "security@example.com"
    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login("you@example.com", "your_password")
        server.send_message(msg)