from inference_sdk import InferenceHTTPClient
import cv2
from SendPush import main
import datetime
import time 

CLIENT = InferenceHTTPClient(
  api_url="https://detect.roboflow.com",
  api_key="TStIa7Kb0ued7inmpIw9"
)
now = datetime.datetime.now()
count = 0
last_minute = now.minute
last_call_time = 0

cap = cv2.VideoCapture(0)

#This function sends the frame to  Roboflow's API and returns a prediction
def getResult(frame):
  result = CLIENT.infer(frame, model_id="fall-detection-v5ye1/1")
  return result


#this function will only return false if called more than once in the cooldown (default is 60s)
def send_notification_with_cooldown(cooldown_time = 60):
  global last_call_time
  current_time = time.time()
  if current_time - last_call_time >= cooldown_time:
    last_call_time = current_time
    return True
  else:
    return False


#this function returns True if it was called 5 times within a minute
def call():
  global now, count, last_minute
  now = datetime.datetime.now()
  if now.minute == last_minute:
    count += 1
    print("count is: ", count)
  else:
    count = 1
    last_minute = now.minute
    print("counter reset")
  #this checks if more than 5 instances of fall were detected, and if no notifications were send in the last cooldown period
  if count >= 5 and send_notification_with_cooldown():
    return True
  else:
    return False

def detect_fall(results):
  if "predictions" in results:
    predictions_list = results["predictions"]
    if len(predictions_list) > 0:
        print("A fall has been detected")
        if(call()):
          main()

def webcam():

  ret, frame = cap.read()

  # Check if frame is captured successfully
  if not ret:
      print("Error: Failed to capture frame")
    
  frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
  result = getResult(frame_rgb)
  detect_fall(result)
  cv2.imshow('Webcam Feed', frame)

def video():
  cap = cv2.VideoCapture("video.mp4")

  while True:
    # Capture frame-by-frame
    ret, frame = cap.read()
    # If the frame is read correctly ret will be True
    if not ret:
      print("No more frames to process!")
      break

    # Get inference result for the frame
    result = getResult(frame)
    cv2.imshow("current frame", frame)    
    detect_fall(result)

# Ask user for input
while True:
  choice = input("Enter 1 for webcam or 2 for video: ")
  if choice in ('1', '2'):
    break
  else:
    print("Enter a valid number")

# Run the selected function
if choice == '1':
  while True:
    webcam()
else:
  video()