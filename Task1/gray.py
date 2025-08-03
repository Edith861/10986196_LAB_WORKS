import cv2


# Load the original image
image = cv2.imread("photo.jpeg")

# Check if the image was loaded correctly
if image is None:
    print("Could not load image. Make sure 'photo.jpg' is in the same folder.")
else:
    # Convert the image to grayscale
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Display both original and grayscale images
    cv2.imshow("Original Image", image)
    cv2.imshow("Grayscale Image", gray_image)

    # Save the grayscale image
    cv2.imwrite("photo_gray.jpg", gray_image)
    print("Grayscale image saved as photo_gray.jpg")

    # Wait for a key press and close image windows
    cv2.waitKey(0)
    cv2.destroyAllWindows()
