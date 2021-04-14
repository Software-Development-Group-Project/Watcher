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


if __name__ == "__main__":
    subject1 = "alert"
    message1 = "put your mask"
    to1 = "thuwarakan123@gmail.com"

    send_email(subject1, message1, to1)
