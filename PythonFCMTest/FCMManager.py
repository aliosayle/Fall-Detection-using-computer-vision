import firebase_admin
from firebase_admin import credentials, messaging
cred = credentials.Certificate("")//replace your firebase credentials 
firebase_admin.initialize_app(cred)

def sendPush(title, msg, registration_token, dataObject=None):
    dataObject = {
        "key1": "value1",
    }
    message = messaging.MulticastMessage(
        notification = messaging.Notification(
            title=title,
            body=msg,
        
        ),
        data=dataObject,
        tokens=registration_token,
    )

    response = messaging.send_multicast(message)

    print("successfully sent message",response)
