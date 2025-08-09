import cv2

def detect_biscuit(image_path):
    # Load image
    image = cv2.imread(image_path)
    if image is None:
        print("Error: Image not found.")
        return None

    # Convert to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Apply Gaussian blur
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)

    # Detect circles (assuming biscuits are circular)
    circles = cv2.HoughCircles(
        blurred, 
        cv2.HOUGH_GRADIENT, 
        dp=1.2, 
        minDist=100, 
        param1=50, 
        param2=30, 
        minRadius=30, 
        maxRadius=80
    )

    # Simple logic: if circles detected, assume "digestive"
    if circles is not None:
        return "digestive"
    else:
        return "unknown"