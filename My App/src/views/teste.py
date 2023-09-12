import cv2 as cv

# Load the image
image = cv.imread('assets/elecLogo.png')

# Check if the image was loaded successfully
if image is None:
    print("Error: Unable to load image.")
else:
    # Display the image in a window
    cv.imshow("Image", image)

    # Wait for a key press and close the window when a key is pressed
    cv.waitKey(0)
    cv.destroyAllWindows()
