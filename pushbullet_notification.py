# from twilio.rest import Client

# account_sid = "ACf19386aa7823318473c44d2be08b3b91"
# auth_token = "60e989e6b6187eb274874de2ed60bb98"
# twilio_number = "+16468080695"
# phone_number = "+919372998994"

# client = Client(account_sid, auth_token)

# message = client.messages.create(
#     body="Hello Grow Fitness I'm Anubhav from Awrim Technologies",
#     from_=twilio_number,
#     to=phone_number
# )
# print(message.body)

# Gmail
import smtplib
from email.message import EmailMessage
def email_alert(subject, body, to):
    msg = EmailMessage()
    msg.set_content(body)
    msg['subject'] = subject
    msg['to'] = to
    user = "yoyoyoyohs05@gmail.com"
    msg['from'] = user
    password = "sbcw gfcb vfxm rpju"
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(user,password)
    server.send_message(msg)
    server.quit()
if __name__ == '__main__':
    email_alert("Hey", "Hello Anubhav", "anubhavtripathi0509@gmail.com")


# SMS
if '@gmail.com' in to:
            self.email_alert(subject, sms_message, to)