#test commit
import cv2
import imutils
import pytesseract

#Read image file
def image(path):
	return cv2.imread(path)

#Pull text from image
def read(image):
	return pytesseract.image_to_string(image)

#Write image to file
def write(image, filename = "modified.jpg"):
	cv2.imwrite(filename, image)

#Crop image to spec
def crop(image, left = 0, right = 0, top = 0, bottom = 0):
	return image[top:bottom, left:right]

#Resize image
def resize(image, height):
	return imutils.resize(image, height = height)

#Grayscale
def grayscale(image):
	return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

#Gaussian Blur
def guassian(image):
	return cv2.GaussianBlur(image, (5, 5), 0)

#Creates an edged image for easier OCR
def edged(image):
	return cv2.Canny(image, 75, 200)

#Noise removal
def removeNoise(image):
	return cv2.medianBlur(image, 5)

#Thresholding 
def thresholding(image):
	return cv2.adaptiveThreshold(image, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)

#Find contours
def findContours(image):
	return cv2.findContours(image, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)

#Sort contours
def sortContours(contours):
	contours = imutils.grab_contours(contours)
	return sorted(contours, key = cv2.contourArea, reverse = True)[:5]

#Draw contours
def drawContours(image, contours):
	for c in contours:
		peri = cv2.arcLength(c, True)
		approx = cv2.approxPolyDP(c, 0.02 * peri, True)
		if len(approx) == 4:
			cv2.drawContours(image, [approx], -1, (0, 255, 0), 3)
			#return approx
