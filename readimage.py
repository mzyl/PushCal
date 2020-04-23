import cv2
import imutils
import pytesseract

#Read image file
def input(path):
	return cv2.imread(path)

#Pull text from image
def read(image):
	return pytesseract.image_to_string(image)

#Write image to file
def write(image, filename = "modified.jpg"):
	cv2.imwrite(filename, image)

#Crop image to spec
def crop(image, left = 0, right = 0, top = 0, bottom = 0):
	return image[0:, 0:int(self.image.shape[1]/2)]

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

#Thresholding - Not sure what this does yet -- Errors anyway
def thresholding(image):
	return cv2.threshold(image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]


