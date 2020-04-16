import cv2
import imutils
import pytesseract

#Read image file
def pathToImage(path):
	return cv2.imread(path)

#Creates an edged image for easier OCR
#Actually seems to work MUCH better without edged
#Resizing is also a factor and produces different results
def imgToEdged(image):
	image = imutils.resize(image, height = 500)
	image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
	image = cv2.GaussianBlur(image, (5, 5), 0)
	return cv2.Canny(image, 75, 200)

#Opens image to verify it looks correctly for troubleshooting
def imgShow(image):
	cv2.imshow("Image", image)
	print("Leave image window open and press any key to close.")
	cv2.waitKey(0)
	cv2.destroyAllWindows()
	cv2.waitKey(1)
	# ***** Something isn't working. Will have to Ctrl-d to close Python to get the window to close. *****

#Reads text from image to be stored in a string
def imgToText(image):
	return pytesseract.image_to_string(image)
