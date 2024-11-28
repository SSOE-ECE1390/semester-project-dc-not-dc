import sys
from attendance import take_attendance, save_attendance, save_png, save_jpeg

"""
Example showing how to use functions in attendance.py
"""
def demo():

    # Check for proper command line arguments
    if len(sys.argv) != 3 and len(sys.argv) != 4:
        sys.exit("Usage: python demo.py -p path_to_image path_to_database")

    # Check for private mode and prepare arguments
    if sys.argv[1] == "-p":
        private_mode = True
        image_path = sys.argv[2]
        database_path = sys.argv[3]
    else:
        private_mode = False
        image_path = sys.argv[1]
        database_path = sys.argv[2]

    # Take attendance 
    img, attendance_dict = take_attendance(image_path, database_path, private = private_mode)

    # Save attendance CSV
    save_attendance(attendance_dict, "attendance.csv")

    # Save image
    save_png(img, "image.png")
    save_jpeg(img, "image.jpg")
    

if __name__ == "__main__":
    demo()
