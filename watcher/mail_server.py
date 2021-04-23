import imghdr
import smtplib
from email.message import EmailMessage
import threading

# pssword for email address
password = "jsexodmjokkpcebg"
# from email address
user = "watchera2019@gmail.com"
# admin email address
admin = "normanjosh567@gmail.com"


class MailServer:
    # initialise the class
    def __init__(self):
        self.server = smtplib.SMTP_SSL("smtp.gmail.com", 465)

    def __del__(self):
        self.server.quit()

    def send_email(self, subject, message, to):

        # creating a Email massage and initalize it to msg
        msg = EmailMessage()
        # setting content
        msg.set_content(message)
        # setting subject
        msg['subject'] = subject
        # setteing the email address where we want to alert
        msg['to'] = to
        # setting a from address
        msg['from'] = user

        # login to the server
        self.server.login(user, password)
        # send_message
        self.server.send_message(msg)

    def create_mail(self, name, to):

        heading = " Watcher (alert) "
        message = "{}, put your mask immediately !".format(name.capitalize())
        adminMessage = "{} is not wearing a mask, please check and notify!".format(
            name.capitalize())

        # sending message to the person who does not wear mask
        self.send_email(heading, message, to)
        # sending message to the admin
        self.send_email(heading, adminMessage, admin)
