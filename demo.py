import cv2
from find_faces import find_faces

def demo():
    
    # Single face detection
    img = cv2.imread("Images/single_face.jpg")

    # Place a bounding box around detected face
    img = find_faces(img)

    # Display image
    cv2.imshow("Face Detection", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    # Multi-face detection
    img = cv2.imread("Images/multiple_faces.jpg")

    # Place a bounding box around detected faces
    img = find_faces(img)

    # Display image
    cv2.imshow("Face Detection", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    return 0

if __name__ == "__main__":
    demo()
