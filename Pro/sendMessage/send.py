import smtplib
from email.message import EmailMessage


def send_email(subject, message, to):
    msg = EmailMessage()
    msg.set_content(message)
    msg['subject'] = subject
    msg['to'] = to

    user = "watchera2019@gmail.com"
    msg['from'] = user
    password = "jsexodmjokkpcebg"

    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(user, password)
    server.send_message(msg)

    server.quit()

def create_mail(name, to):
    admin = "thuwarakan123@gmail.com"
    heading = " Watcher (alert) "
    message ="{}, put your mask immediately" .format(name)
    adminMessage = "{} is not wear a mask, please check" .format(name)
    send_email(heading, message, to)
    send_email(heading, adminMessage, admin)


if __name__ == "__main__":
    name = "vithushigan"
    to1 = "mailto:jayavithushigan@gmail.com"
    
    create_mail(name, to1)
