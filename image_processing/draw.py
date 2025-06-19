import cv2

def draw_red_circle(img, x, y, radius):
    """
    Draws a red circle on the image.
    Returns the modified image or the original if an error occurs.
    """
    try:
        x = int(x)
        y = int(y)
        radius = int(radius)
        if radius <= 0:
            raise ValueError("Radius must be a positive integer.")
        # Draw red circle (BGR: (0, 0, 255))
        return cv2.circle(img, (x, y), radius, (0, 0, 255), 2)
    except ValueError as e:
        print(f"Circle drawing error: {e}")
        return img