import cv2
from deepface import DeepFace
import matplotlib.pyplot as plt
import os
import pandas as pd


"""
Takes attendance by identifying faces within input image and attempting to find a match in the database. 
Annotates image with bounding boxes labelled with either the name of the matched attendee or a message
indicating a match was not found. Returns annotated image along with a dictionary containing all expected
attendees and whether or not they were present. 

Parameters:
    * img: Path to image that will be searched for faces.
    * database: Path to database of known faces. 
    * private: Boolean that determines whether Privacy Mode is enabled. If True, all detected faces are blurred. 

Additional information: For best results, each image in the database should contain only one face and be
named in the format name.jpg, name.png, etc. The code extracts the name of the individual in the image
by splitting the image name on the period.    
"""
def take_attendance(img_path, database_path, private = False):

    # Create dictionary of names and face coordinates
    attendees = {}

    # Initialize attendance dictionary
    attendance_dict = create_attendee_dict(database_path)

    # Read image
    img = cv2.imread(img_path)

    # Detect all faces in the image
    analysis = DeepFace.analyze(img_path)

    # Analyze each detected face
    for face in analysis:

        # Get the face's bounding box coordinates 
        face_region = face["region"]
        x, y, w, h = face_region["x"], face_region["y"], face_region["w"], face_region["h"]

        # Crop the face from the image using the bounding box
        face_crop = img[y:y + h, x:x + w]

        # Use DeepFace to identify the most similar face in the database (based on the cropped face)
        result = DeepFace.find(face_crop, database_path, enforce_detection = False)

        # Check if result contains any non-empty DataFrames
        for result_df in result:
            if not result_df.empty:

                # Access the first match's identity if the DataFrame is not empty
                matched_image_path = result_df['identity'].values[0]

                # Extract the name of the person from the filename (assuming name.png/jpg/etc. format)
                person_name = os.path.basename(matched_image_path).split('.')[0]

                # Update attendance dictionary
                attendance_dict[person_name] = True
                
            else:
                person_name = "UNIDENTIFIED"

        # Record attendee
        attendees[person_name] = (x, y, w, h)

    # Modify image with bounding boxes and labels 
    for attendee in attendees.keys():

        # Unpack coordinates
        x = attendees[attendee][0]
        y = attendees[attendee][1]
        w = attendees[attendee][2]
        h = attendees[attendee][3]

        # Label the bounding box
        cv2.putText(img, attendee, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 1.0, (0, 255, 0), 2)

        # If in Privacy Mode, blur detected face
        if private:
            privacy_blur(img, x, y, w, h)

        # Draw bounding box around the face
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)

    # Convert image to RGB and display
    rgb_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    plt.imshow(rgb_img)
    plt.show()

    return img, attendance_dict


"""
Save attendance dictionary as CSV file. Prints a warning if there is an unidentified attendee. 

Parameters:
    * attendance_dict: Dictionary of attendees. 
"""
def save_attendance(attendance_dict, file_path):

    # Pandas workaround: must make all dictionary entries a list
    for attendee in attendance_dict.keys():
        attendance_dict[attendee] = [attendance_dict[attendee]]

    # Print a warning if there is an unidentified attendee
    if "UNIDENTIFIED" in attendance_dict.keys():
        print("WARNING: Unidentified attendee detected. Verify attendance record.")
    
    # Create and save as a Pandas DataFrame
    df = pd.DataFrame(attendance_dict)
    df.to_csv(file_path, index = False)


"""
Save image as PNG (no loss compression).

Parameters:
    * img: Image to be saved.
    * file_path: Destination for image (image should be .png). 
"""
def save_png(img, file_path):
    cv2.imwrite(file_path, img)
    print(f"Image saved as {file_path} (PNG, lossless compression).")


"""
Save image as JPEG (lossy compression).

Parameters: 
    * img: Image to be saved.
    * file_path: Destination for image (image should be .jpg)
"""
def save_jpeg(img, file_path):

    # Set compression parameters (quality level for JPEG)
    encode_param = [int(cv2.IMWRITE_JPEG_QUALITY), 90]
    cv2.imwrite(file_path, img, encode_param)
    print(f"Image saved as {file_path} (JPEG, quality = 90, lossy compression).")


"""
Blur faces for privacy.

Parameters:
    * img: Image to be blurred.
    * x: x-coordinate of upper left corner of face
    * y: y-coordinate of upper left corner of face
    * w: width of face
    * h: height of face
"""
def privacy_blur(img, x, y, w, h):

    # Extract the face 
    face_region = img[y:y + h, x:x + w]

    # Apply Gaussian blur to the face 
    blurred_face = cv2.GaussianBlur(face_region, (99, 99), 30)

    # Replace original face with blurred face
    img[y:y + h, x:x + w] = blurred_face


"""
Creates expected attendee dictionary from database. Returns the dictionary with all names initialized to False
(not present). 

Parameters:
    * database_path: Path to database.
"""
def create_attendee_dict(database_path):
    
    # Construct attendance dictionary
    attendance_dict = {}
    for filename in os.listdir(database_path):

        # Extract attendee name and create dictionary entry
        if '.' in filename:
            name = filename.split('.')[0]
            attendance_dict[name] = False

    return attendance_dict