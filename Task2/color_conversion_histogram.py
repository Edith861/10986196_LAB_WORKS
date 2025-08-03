import cv2
import matplotlib.pyplot as plt

# Load the color image
image = cv2.imread("photo.jpeg")

if image is None:
    print("Could not load image. Make sure 'photo.jpg' exists in this folder.")
    exit()

# Convert to Grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow("Grayscale", gray)
cv2.imwrite("photo_grayscale.jpg", gray)

# Convert to HSV
hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
cv2.imshow("HSV", hsv)
cv2.imwrite("photo_hsv.jpg", hsv)

# Convert to LAB
lab = cv2.cvtColor(image, cv2.COLOR_BGR2Lab)
cv2.imshow("LAB", lab)
cv2.imwrite("photo_lab.jpg", lab)

# Plot grayscale histogram
plt.figure(figsize=(6, 4))
plt.hist(gray.ravel(), bins=256, range=[0, 256], color='gray')
plt.title('Grayscale Histogram')
plt.xlabel('Pixel Intensity')
plt.ylabel('Frequency')
plt.grid(True)
plt.tight_layout()
plt.show()

# Wait for key press and close image windows
cv2.waitKey(0)
cv2.destroyAllWindows()
