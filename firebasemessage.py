import firebase_admin
from firebase_admin import credentials, messaging

cred = credentials.Certificate('./firebasecredential.json')
firebase_admin.initialize_app(cred)
message = messaging.Message(
    notification=messaging.Notification(
        title="Your message title",  # Optional
        body="Your message body"
    ),
    token="FCM_token_of_the_device"  # Replace with the actual device token
)
response = messaging.send(message)
print(response)