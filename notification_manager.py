from twilio.rest import Client
import smtplib
TWILIO_SID = "AC70edcf6b9b626663766a294ed436c645"
TWILIO_AUTH_TOKEN = "b9305333dc5ccc23a612edc311cb42d0"
TWILIO_VIRTUAL_NUMBER = "+15855952533"
TWILIO_VERIFIED_NUMBER = "+886982212727"
MY_EMAIL = "traderjacob0607@gmail.com"
MY_PASSWORD = "hdruzrceltaxudbo"


class NotificationManager:
    # This class is responsible for sending notifications with the deal flight details.
    def __init__(self):
        self.client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

    def send_sms(self, message):
        message = self.client.messages.create(
            body=message,
            from_=TWILIO_VIRTUAL_NUMBER,
            to=TWILIO_VERIFIED_NUMBER
        )
        print(message.sid)

    def send_emails(self, emails, message, google_flight_link):
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=MY_PASSWORD)
            for email in emails:
                connection.sendmail(
                    from_addr=MY_EMAIL,
                    to_addrs=email,
                    msg=f"Subject:New Low Price Flight!\n\n{message}\n{google_flight_link}".encode('utf-8')
                )
