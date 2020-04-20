#Not much more to do here until new calendar layout is made
import cv2
import imutils
import pytesseract

#Read image file
def pathToImage(path):
	return cv2.imread(path)

#Creates an edged image for easier OCR
#Not actually great for OCR, but may be useful later
def toEdged(image):
	return cv2.Canny(image, 75, 200)

#Resize image
def resize(image, height):
	return imutils.resize(image, height = height)

#Gaussian Blur
def guassian(image):
	return cv2.GaussianBlur(image, (5, 5), 0)

#Noise removal
def removeNoise(image):
	return cv2.medianBlur(image, 5)

#Thresholding - Not sure what this does yet
#Errors anyway...
def thresholding(image):
	return cv2.threshold(image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]

#Grayscale
def gray(image):
	return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

#Reads text from image to be stored in a string
def toText(image):
	return pytesseract.image_to_string(image)

#Writes image to file instead of using cv2.imshow to view image through Python window
def write(image):
	cv2.imwrite("modified.jpg", image)

#Makes a separate image for the days to be read from
def splitDays(image):
	return image[0:, 0:int(image.shape[1]/2)]

#Makes a separate image for the times to be read from
def splitTimes(image):
	return image[0:, int(image.shape[1]/2):]

#config = r'--oem 3 -psm *'
#pytesseract.image_to_string(x, config=config)
#psm 3 works best for Days
#psm 12 works best for Times

