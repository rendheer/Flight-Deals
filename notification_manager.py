from twilio.rest import Client
import smtplib

class NotificationManager:
    #This class is responsible for sending notifications with the deal flight details.
    def __init__(self):
        self.TWILIO_SID = "AC4d455acba5fd6e26b56b7869e25b13a8"
        self.TWILIO_AUTH_TOKEN = "4b3ab636d02afebff43f01e7b47ff2a7"
        self.VIRTUAL_TWILIO_NUMBER = "+18456979245"
        self.VERIFIED_NUMBER = "+14088768780"
        self.MY_EMAIL = "rendheer_joshy@yahoo.com"
        self.MY_PASSWORD = "toxjwadamcckymbh"

    def send_notification(self, msg_body):
        client = Client(self.TWILIO_SID, self.TWILIO_AUTH_TOKEN)
        message = client.messages.create(
            body=msg_body,
            from_=self.VIRTUAL_TWILIO_NUMBER,
            to=self.VERIFIED_NUMBER
        )

    def send_emails(self, email, message):
        with smtplib.SMTP("smtp.mail.yahoo.com", port=587) as connection:
            connection.starttls()
            connection.login(self.MY_EMAIL, self.MY_PASSWORD)

            connection.sendmail(
                from_addr=self.MY_EMAIL,
                to_addrs=email,
                msg=f"Subject:New Low Price Flight!\n\n{message}"
            )