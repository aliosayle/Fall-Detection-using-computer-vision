import sys
from inference_sdk import InferenceHTTPClient
import cv2
from SendPush import main
import datetime
import time 
from colorama import Fore, Style

CLIENT = InferenceHTTPClient(
  api_url="https://detect.roboflow.com",
  api_key=""
 <b> //Please replace your api key</b>
)
now = datetime.datetime.now()
count = 0
threshold = 5 #this changes how many detection per mintute will result in notification being sent
cooldown = 60 #this changes how much time between each notification being sent
last_minute = now.minute 
last_call_time = 0
verbose = 1

cap = cv2.VideoCapture(0)

def loading_animation(add_dot=True, duration=5, interval=0.5):
  if(verbose == 2 or verbose == 3):
    print("frame analysed, no fall detected")

#This function sends the frame to  Roboflow's API and returns a prediction
def getResult(frame):
  result = CLIENT.infer(frame, model_id="fall-detection-v5ye1/1")
  return result


#this function will only return false if called more than once in the cooldown (default is 60s)
def send_notification_with_cooldown(cooldown_time = cooldown):
  global last_call_time
  current_time = time.time()
  if current_time - last_call_time >= cooldown_time:
    last_call_time = current_time
    return True
  else:
    return False


#this function returns True if it was called (threshold) times within a minute
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
  if count >= threshold and send_notification_with_cooldown():
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
    loading_animation()
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
  choice = input("Enter 1 for webcam or 2 for video or 3 for setup: ")
  if choice in ('1', '2', '3'):
    break
  else:
    print("Enter a valid number")

# Run the selected function
if choice == '1':
  while True:
    webcam()
elif choice == '2':
  video()
else:
  print("setup mode")
  threshold = int(input("enter the threshold, or how many detections per minute will result in a notification: "))
  coolddown = int(input("enter the cooldown for notifications in seconds(default is 60): "))
  verbose = int(input("verbose(1,2 or 3): "))
  print("setup complete")
  choice = input("choose 1 for webcam or 2 for test vid: ")
  if choice == 1:
    while True:
      webcam()
  else:
    video()
