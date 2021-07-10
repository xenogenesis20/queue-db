# Download the helper library from https://www.twilio.com/docs/python/install
import os
from twilio.rest import Client

# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure
def send_msg(body="somebody",to=""):
    account_sid = os.environ['TWILLIO_SID']
    auth_token = os.environ['TWILLIO_AUTH_TOKEN']
    client = Client(account_sid, auth_token)
    twillio_phone_number = os.environ['TWILLIO_PHONE_NUMBER']
    my_phone_number = os.environ['MY_PHONE_NUMBER']

    message = client.messages.create(
                                body=body,
                                from_=twillio_phone_number,
                                to=my_phone_number
                            )

    print(message.sid)

