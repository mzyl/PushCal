import cv2
import imutils
import pytesseract

#Read image file
def image(path):
	return cv2.imread(path)

#Pull text from image
def read(image, x = 12):
	config = r'--oem 3 --psm {}'.format(x)
	return pytesseract.image_to_string(image, config = config)

#Write image to file
def write(image, filename = "modified.jpg"):
	cv2.imwrite(filename, image)

#Crop image to spec
def crop(image, left = None, right = None, top = None, bottom = None):
	return image[top:bottom, left:right]

#Resize image
def resize(image, height):
	return imutils.resize(image, height = height)

'''Image modification functions'''

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
def noise_removal(image):
	return cv2.medianBlur(image, 5)

#Thresholding 
def thresholding(image):
	return cv2.adaptiveThreshold(image, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)

'''Contour/Line mapping functions'''

#Find contours
def find_contours(image):
	return cv2.findContours(image, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)

#Sort contours
def sort_contours(contours):
	contours = imutils.grab_contours(contours)
	return sorted(contours, key = cv2.contourArea, reverse = True)[:5]

#Draw contours
def draw_contours(image, contours):
	array = []
	for c in contours:
		peri = cv2.arcLength(c, True)
		approx = cv2.approxPolyDP(c, 0.02 * peri, True)
		if len(approx) == 4:
			cv2.drawContours(image, [approx], -1, (0, 255, 0), 3)
			array.append(approx)
	return array

'''Frequent combo functions'''

def prep_for_contours(image):
	image = grayscale(image)
	image = removeNoise(image)
	return thresholding(image)

def do_contours(draw, image):
	contours = findContours(image)
	contours = sortContours(contours)
	return drawContours(draw, contours)

''' To Do:
Find better way to find boxes.
	Word boxes to lines idea?
	Just lines to lines using horizontals?
Automate cropping from contour points.
Remove noise from text.
Begin interacting with Dates Class.
'''
