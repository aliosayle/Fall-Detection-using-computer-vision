import FCMManager as fcm

def main():
  tokens = ["f17oqJgwS1qb7t3G6oNF7S:APA91bHj5phk3-pqbEUT6AHpkLtn_CGvdCOdAY83-c2o-vb70kiWfDvQnnV6c4R7_gGhKa5mu8p-FI-lQSyW_xE50Wk2Bvmp69vhuwQyOkAsz3kdXCSZ5zgIS1Ecy9skV0jbaaLWLT6m"]
  fcm.sendPush("\U0001F4F8 Fall 490 ", "Fall has been detected, Please check your app now", tokens)

if __name__ == "__main__":
  main()
