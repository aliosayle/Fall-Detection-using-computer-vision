import firebase_admin
from firebase_admin import credentials, messaging
cred = credentials.Certificate("C:\\Users\\USER\\OneDrive\\Desktop\\PythonFCMTest\\python-fcm-test-c2685-firebase-adminsdk-1gz7v-0f0c6d3bae.json")

# cred = credentials.Certificate("C:\Users\USER\OneDrive\Desktop\PythonFCMTest\python-fcm-test-c2685-firebase-adminsdk-1gz7v-0f0c6d3bae.json")
firebase_admin.initialize_app(cred)

def sendPush(title, msg, registration_token, dataObject=None):

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