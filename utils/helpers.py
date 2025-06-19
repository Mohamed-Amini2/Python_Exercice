import cv2

def load_image(path):
    """Loads an image and checks the file format."""
    if not path.lower().endswith(('.png', '.jpg', '.jpeg')):
        print("Error: Only .png or .jpg formats are supported.")
        return None
    
    img = cv2.imread(path)
    if img is None:
        print("Error: Unable to load image. Check the file path.")
    return img

def save_image(img, output_path):
    """Saves the image to the specified path."""
    try:
        cv2.imwrite(output_path, img)
        print(f"Image saved to {output_path}")
    except Exception as e:
        print(f"Error saving image: {e}")

def validate_numeric_input(value, min_value=0):
    """Validates numeric input and ensures it's >= min_value."""
    try:
        value = int(value)
        if value < min_value:
            raise ValueError(f"Value must be at least {min_value}.")
        return value
    except ValueError as e:
        print(f"Input error: {e}")
        return None