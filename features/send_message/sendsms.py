
import os
from twilio.rest import Client


account_sid = 'ACa3fb902cf40514d58fc5d1d67ba12772'
auth_token = '2ef7248acc880926a192489b0769d71c'
client = Client(account_sid, auth_token)
adminNumber = "+94766008160"

def create_message(number, name):
     
    message = client.messages \
        .create(
            body="{}, put your mask immediately" .format(name),
            from_='+12392304394',
            to=number
        )

    message = client.messages \
        .create(
            body="{}, is not wear a mask, please check" .format(name),
            from_='+12392304394',
            to= "+94766008160"
        )

to = "+94773077740"
name = "jenoshanan"
create_message(to, name)

 