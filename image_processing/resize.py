import cv2

def resize_image(img, width, height):
    """
    Resizes the image to the specified dimensions.
    Returns the resized image or the original if an error occurs.
    """
    try:
        width = int(width)
        height = int(height)
        if width <= 0 or height <= 0:
            raise ValueError("Width and height must be positive integers.")
        return cv2.resize(img, (width, height))
    except ValueError as e:
        print(f"Resize error: {e}")
        return img