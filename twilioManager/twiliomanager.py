from twilio.rest import Client
import os


class TwilioManager:
    def __init__(self):
        account_sid = os.environ['TWILIO_ACCOUNT_SID']
        auth_token = os.environ['TWILIO_AUTH_TOKEN']
        self.client = Client(account_sid, auth_token)

    def message(self, userMessage: str) -> int:
        message = self.client.messages.create(
            body=userMessage,
            from_="+13853991897",
            to=os.environ["VERIFY_CALLER_ID"])
