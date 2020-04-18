import cv2
import imutils
import pytesseract

#Read image file
def pathToImage(path):
	return cv2.imread(path)

#Creates an edged image for easier OCR
#Actually seems to work MUCH better without edged
#Resizing is also a factor and produces different results
def toEdged(image):
	image = imutils.resize(image, height = 500)
	image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
	image = cv2.GaussianBlur(image, (5, 5), 0)
	return cv2.Canny(image, 75, 200)

#Reads text from image to be stored in a string
def toText(image):
	return pytesseract.image_to_string(image)

#Writes image to file instead of using cv2.imshow to view image through Python window
def write(image):
	cv2.imwrite("modified.jpg", image)

def splitImage(image, c1, c2):
	c1 = image[0:, 0:int(image.shape[1]/2)]
	c2 = image[0:, int(image.shape[1]/2):]
