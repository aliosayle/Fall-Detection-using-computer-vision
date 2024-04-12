from inference_sdk import InferenceHTTPClient
import cv2

CLIENT = InferenceHTTPClient(
  api_url="https://detect.roboflow.com",
  api_key="TStIa7Kb0ued7inmpIw9"
)

cap = cv2.VideoCapture(0)

#This function sends the frame to  Roboflow's API and returns a prediction
def getResult(frame):
  result = CLIENT.infer(frame, model_id="fall-detection-v5ye1/1")
  return result

def webcam():

  ret, frame = cap.read()

  # Check if frame is captured successfully
  if not ret:
      print("Error: Failed to capture frame")
    
  frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

  result = getResult(frame_rgb)
  
  print(result)

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
    # Print the result
    print(result)

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