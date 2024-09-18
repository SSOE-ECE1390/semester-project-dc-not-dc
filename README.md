[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/tdy6BFPL)
[![Open in Visual Studio Code](https://classroom.github.com/assets/open-in-vscode-2e0aaae1b6195c2367325f4f02e2d04e9abb55f0b24a779b69b11b9e10269abc.svg)](https://classroom.github.com/online_ide?assignment_repo_id=16029241&assignment_repo_type=AssignmentRepo)
# ece-1390-project

## Description
We will be creating an automatic attendance taker. We believe this will reduce the burden on class instructors, who often must set aside valuable lecture time to record attendance in classes where it is required. Additionally, the data from this attendance taker may offer insight into student attendance patterns over time and help identify at-risk students based on class attendance. The target consumer of the product is any user who may benefit from the ability to quickly collect and analyze attendance data for classes, meetings, and other scenarios. 

## Code Specifications
The expected input is a still frame image of file format .jpg and .png. The output of the program will be the input image with all faces within bounding boxes and a count of the total number of people in the image. There will also be an outputted .csv file indicating the name of each enrolled student and whether or not they have been counted as present.    

## Planned approach
This project will be implemented with Python and OpenCV. As per the project specifications, we will include the ability to process still images, methods to enhance and filter the input image, and the use of edge detection, segmentation and object recognition. We plan to use YOLO for object detection and recognition. If we have time, we will include additional functionality: we will add the ability to include video input for dynamic attendance taking over time and annotate the bounding boxes with the names of the students.   

## Timeline
We expect this progress to be completed over the course of the semester. By the end of this month, we plan to have object detection via bounding boxes implemented to recognize a person. By the end of October, we hope to recognize multiple distinct faces within an image and count the number of distinct faces. We also hope to include the other required methods - image filtering and enhancement, etc. By the end of November, we hope to have a coordinate system in place to map expected attendees to certain points in the image (for example, an assigned seat) and use this mapping system to determine if an expected attendee is present or not. We are aiming to have the entire project working by the end of November, leaving time for improvements and additions during December if desired.   

## Success Metrics
We will define success as meeting the basic goals of the project: including all project requirements and achieving basic functionality (face detection and counting, location mapping). 

## Pitfalls and alternative solutions
We may face issues when designing a coordinate system that must match the location of a specific face to an expected location. If this occurs, we will redefine sucess to be identifying and counting faces, leaving the decision of who is actually present or absent to the instructor. 
