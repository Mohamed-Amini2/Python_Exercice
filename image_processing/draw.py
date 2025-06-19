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
        
        # Validate input
        if radius <= 0:
            raise ValueError("Radius must be a positive integer.")
        if x < 0 or y < 0 or x >= img.shape[1] or y >= img.shape[0]:
            raise ValueError(f"Coordinates must be within image dimensions: (0-{img.shape[1]}, 0-{img.shape[0]})")

        # Draw red circle (BGR: (0, 0, 255))
        return cv2.circle(img, (x, y), radius, (0, 0, 255), 2)
    except ValueError as e:
        print(f"Circle drawing error: {e}")
        return img