import smtplib
from email.message import EmailMessage


def send_email(subject, message, to):
    msg = EmailMessage()
    msg.set_content(message)
    msg['subject'] = subject
    msg['to'] = to

    user = "normanjosh567@gmail.com"
    msg['from'] = user
    password = "apigkdmldagyjicn"

    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(user, password)
    server.send_message(msg)

    server.quit()

def create_mail(name, to):
    heading = " Watcher (alert) "
    message ="{}, put your mask immediately" .format(name)
    send_email(heading, message, to)


if __name__ == "__main__":
    name = "vithushigan"
    to1 = "mailto:jayavithushigan@gmail.com"
    
    create_mail(name, to1)
