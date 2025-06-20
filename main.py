import cv2
from utils.helpers import load_image, save_image
from image_processing.resize import resize_image
from image_processing.brightness import decrease_brightness
from image_processing.draw import draw_red_circle
import numpy as np

def show_channels(img):
    """Displays the red, green, and blue channels of the image."""
    channels = {
        "Red": cv2.merge([img[:, :, 0],
            np.zeros_like(img[:, :, 1]),
            np.zeros_like(img[:, :, 2])]),
        "Green": cv2.merge([np.zeros_like(img[:, :, 0]),
            img[:, :, 1], 
            np.zeros_like(img[:, :, 2])]),
        "Blue": cv2.merge([np.zeros_like(img[:, :, 0]),
            np.zeros_like(img[:, :, 1]),
            img[:, :, 2]])
    }
    for name, channel in channels.items():
        cv2.imshow(f"{name} Channel", channel)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

def capture_from_webcam():
    """Takes a photo from the webcam."""
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("Error: Unable to connect to the webcam.")
        return None
    ret, frame = cap.read()
    cap.release()
    if not ret:
        print("Error: Unable to capture image from webcam.")
        return None
    return frame

def main():
    print("Welcome to the Image Processing App!")
    
    img = None
    while img is None:
        print("\nChoose how to get the image:")
        print("1. Load from file")
        print("2. Capture from webcam")
        choice = input("Enter 1 or 2: ")

        if choice == "1":
            image_path = input("Enter image path: ")
            img = load_image(image_path)
        elif choice == "2":
            print("Connecting to webcam...")
            img = capture_from_webcam()
        else:
            print("Invalid choice. Try again.")
        
        if img is None:
            print("Please try again with a valid image source.")

    cv2.imshow("Original Image", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    show_channels(img)
    print("\nChoose an action:")
    print("1. Resize Image")
    print("8. Decrease Brightness")
    print("13. Draw Red Circle")
    task = input("Enter task number (1/8/13): ")

    if task == "1":
        width = input("Enter target width: ")
        height = input("Enter target height: ")
        img = resize_image(img, width, height)
    elif task == "8":
        value = input("Enter brightness decrease value: ")
        img = decrease_brightness(img, value)
    elif task == "13":
        x = input("Enter X coordinate of the circle center: ")
        y = input("Enter Y coordinate of the circle center: ")
        radius = input("Enter circle radius: ")
        img = draw_red_circle(img, x, y, radius)
    else:
        print("Invalid task selection.")
        return

    cv2.imshow("Result", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    save_path = input("Enter output file path (e.g., output.jpg): ")
    save_image(img, save_path)

if __name__ == "__main__":
    main()