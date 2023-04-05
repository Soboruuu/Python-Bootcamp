import os
from twilio.rest import Client

class Twilio():
    def __init__(self,message):
        self.twilio_sid = os.environ.get('TWILIO_SID')
        self.twilio_token = os.environ.get('TWILIO_TOKEN')
        self.client = Client(self.twilio_sid, self.twilio_token)
        self.message = self.client.messages \
            .create(
            body=message,
            from_=os.environ.get('TWILIO_NUMBER'),
            to=os.environ.get('MY_NUMBER')
        )
        print(self.message.status)