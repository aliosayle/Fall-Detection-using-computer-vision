import FCMManager as fcm


def main():
  tokens=[""] #replace this with you actual key from firebase
  fcm.sendPush("\U0001F4F8 Fall 490 ", "Fall has been detected, Please check your app now",tokens)

if __name__ == "__main__":
  main()

