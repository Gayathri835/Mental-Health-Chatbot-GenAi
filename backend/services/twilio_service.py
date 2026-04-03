from twilio.rest import Client
import os

def trigger_alert(message: str):
    client = Client(
        os.getenv("TWILIO_SID"),
        os.getenv("TWILIO_AUTH")
    )

    client.messages.create(
        body=f"Crisis Alert: {message}",
        from_="+1234567890",
        to="+919XXXXXXXXX"
    )
