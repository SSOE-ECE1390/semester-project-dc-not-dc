[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/tdy6BFPL)
[![Open in Visual Studio Code](https://classroom.github.com/assets/open-in-vscode-2e0aaae1b6195c2367325f4f02e2d04e9abb55f0b24a779b69b11b9e10269abc.svg)](https://classroom.github.com/online_ide?assignment_repo_id=16029241&assignment_repo_type=AssignmentRepo)
# ece-1390-project

## Description
We have created an automatic attendance taker. We believe this will reduce the burden on class instructors, who often must set aside valuable lecture time to record attendance in classes where it is required. Additionally, the data from this attendance taker may offer insight into student attendance patterns over time and help identify at-risk students based on class attendance. The target consumer of the product is any user who may benefit from the ability to quickly collect and analyze attendance data for classes, meetings, and other scenarios. 

## Code Specifications
The expected input is a still frame image of file format .jpg, .jpeg, or .png along with a database containing images of all expected attendees. An optional input enables Privacy Mode, which blurs all detected faces. There are functions that optionally save the attendees as a CSV file, and the resulting image may be saved as a .png or .jpg file. Our most important function, take_attendance, creates an image with bounding boxes around each face; it also attempts to label each face with a name pulled from that attendee's image in the database. If a matching face in the database isn't found, that attendee is marked as unidentified. The take_attendance function also returns a dictionary containing each name in the database and whether the associated attendee was found in the image or not (present or absent)      

## Approach
This project was implemented with Python, OpenCV, and deepface. We tried several different libraries for the facial recognition feature - Haar cascades with OpenCV, MediaPipe, and finally deepface. Haar cascades were far too inaccurate for our use case while MediaPipe proved to be too limited. deepface is able to both find faces in an image and compare these faces to a database to check for a match, which suited our use case. OpenCV is used for supplemental functions like blurring in Privacy Mode and saving images in different formats.   

## Timeline
We met our timeline goal of completing our base requirements by the end of November. We will work on final touches in December before presenting to the class. 

## Success Metrics
OLD: We will define success as meeting the basic goals of the project: including all project requirements and achieving basic functionality (face detection and counting, location mapping). 
UPDATED: When we discovered deepface, we realized we could make a much more robust attendance taker. Our original idea was to create an initial attendance board where faces would be mapped to expected location (it wouldn't be able to identify a specific face, just the presence of a generic face). An attendance photo would be fed in, and we would calculate whether a face was within the expected range. This would determine whether an attendee was present or absent. With deepface, we can search the entire image for specific faces, which only requires a pre-existing database of attendee images. It also removed our requirement that the attendance picture always be taken from the same angle. Our new solution is much more robust, and so we've decided that we have exceeded our original success metrics. 

## Pitfalls and alternative solutions
We faced pitfalls when deciding what face detection solution to use, but were able to pivot and find a satisfactory solution that actually improved our final attendance taker. We also struggled with time management but were able to create a project that met our requirements. 

## Usage
All relevant functions are in attendance.py. The file demo.py provides an example of how these functions may be used with command-line arguments. Run demo.py using:
python demo.py path_to_image path_to_database
An optional -p flag can be used to enable "privacy mode," where images are displayed and saved with the faces obscured by a blurring effect:
python demo.py -p path_to_image path_to_database
