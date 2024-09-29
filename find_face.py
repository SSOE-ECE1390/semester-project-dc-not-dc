import cv2
import mediapipe as mp
from mediapipe.tasks import python
from mediapipe.tasks.python import vision


"""
This function accepts a BGR image and places bounding boxes around all faces detected in the image.
"""
def find_faces(img):

    # Initialize MediaPipe face detection functionality
    mp_face_detection = mp.solutions.face_detection

    # Create an instance of MediaPipe face detection model
    face_detection = mp_face_detection.FaceDetection(min_detection_confidence = 0.5)

    # Convert the image to RGB
    rgb_image = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    # Detect faces
    results = face_detection.process(rgb_image)

    # Determine if any faces were detected
    if results.detections:

        # Place bounding boxes around detected faces
        for detection in results.detections:

            # Obtain bounding box coordinates
            coords = detection.location_data.relative_bounding_box
            h, w, _ = img.shape
            x, y, width, height = (coords.xmin * w, coords.ymin * h, 
                                   coords.width * w, coords.height * h)

            # Convert to integers for drawing
            x, y, width, height = int(x), int(y), int(width), int(height)
            
            # Draw the bounding box
            cv2.rectangle(img, (x, y), (x + width, y + height), (0, 0, 255), 2)

    # Return the modified image
    return img

