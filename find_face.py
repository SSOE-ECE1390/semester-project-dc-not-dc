import cv2


"""
This function accepts a BGR image (should contain at least one recognizable human face)
and places a bounding box around all faces detected in the image.

Adapted from TutorialsPoint: 
https://www.tutorialspoint.com/how-to-detect-a-face-and-draw-a-bounding-box-around-it-using-opencv-python

Tasks: replace with a different classifier (YOLO?)
"""
def find_faces(img):

    # Convert image to grayscale (note BGR color scheme)
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Haar cascade detects faces in input image
    hc = cv2.CascadeClassifier("haarcascade_frontalface_alt.xml")

    # Detect faces
    faces = hc.detectMultiScale(gray_img, 1.1, 2)

    # Place bounding boxes around all detected faces
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 255), 2)
    
    # Function returns the modified image
    return img
    
