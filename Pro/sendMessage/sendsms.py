
import os
from twilio.rest import Client


account_sid = 'ACa3fb902cf40514d58fc5d1d67ba12772'
auth_token = '2ef7248acc880926a192489b0769d71c'
client = Client(account_sid, auth_token)

message = client.messages \
    .create(
        body='Please put your Mask',
        from_='+12392304394',
        to='+94766008160'
    )

print(message.sid)
