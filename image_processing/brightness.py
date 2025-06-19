import numpy as np

def decrease_brightness(img, value):
    """
    Decreases brightness by subtracting a value from each pixel.
    Returns the adjusted image or the original if an error occurs.
    """
    try:
        value = int(value)
        if value < 0:
            raise ValueError("Brightness value must be non-negative.")
        # Subtract value from all pixels, clamping to 0-255 range
        return np.clip(img.astype(int) - value, 0, 255).astype(np.uint8)
    except ValueError as e:
        print(f"Brightness error: {e}")
        return img