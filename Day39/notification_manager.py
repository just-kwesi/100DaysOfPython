from twilio.rest import Client
from dotenv import dotenv_values

CONFIG = dotenv_values("env")


class NotificationManager:
    def __init__(self):
        self.account_sid = CONFIG['TWILIO_ACCOUNT_SID']
        self.auth_token = CONFIG['TWILIO_AUTH_TOKEN']

    def sendMessage(self, message):
        client = Client(self.account_sid, self.auth_token)

        message = client.messages \
            .create(
            body = message,
            from_='+15133275938',
            to = '+17184154873'
        )
        return message.sid
