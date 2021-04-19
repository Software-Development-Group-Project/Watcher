import imghdr
import smtplib
from email.message import EmailMessage
import threading

password = "jsexodmjokkpcebg"
user = "watchera2019@gmail.com"
admin = "thuwarakan123@gmail.com"


class MailServer:

    def __init__(self):
        self.server = smtplib.SMTP_SSL("smtp.gmail.com", 465)

    def __del__(self):
        self.server.quit()

    def send_email(self, subject, message, to):

        msg = EmailMessage()
        msg.set_content(message)
        msg['subject'] = subject
        msg['to'] = to
        msg['from'] = user

        self.server.login(user, password)
        self.server.send_message(msg)

    def create_mail(self, name, to):
        heading = " Watcher (alert) "
        message = "{}, put your mask immediately".format(name.capitalize())
        adminMessage = "{} is not wearing a mask, please check".format(name.capitalize())

        self.send_email(heading, message, to)
        self.send_email(heading, adminMessage, admin)