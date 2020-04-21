import cv2
import imutils
import pytesseract

#Maybe a subclass should be made to handle image modification?

class Image():

	#Read image file
	def __init__(self, path):
		self.image = cv2.imread(path)

	#Return image contents
	def ret(self):
		return self.image

	#Grayscale
	def gray(self):
		self.image = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)

	#Resize image
	def resize(self, height):
		self.image = imutils.resize(self.image, height = height)
	
	#Gaussian Blur
	def guassian(image):
		return cv2.GaussianBlur(image, (5, 5), 0)

	#Creates an edged image for easier OCR
	def toEdged(image):
		return cv2.Canny(image, 75, 200)

	#Noise removal
	def removeNoise(image):
		return cv2.medianBlur(image, 5)

	#Thresholding - Not sure what this does yet -- Errors anyway
	def thresholding(image):
		return cv2.threshold(image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]

	#Pull text from image
	def read(self):
		return pytesseract.image_to_string(self.image)

	#Write image to file
	def write(self, filename = "modified.jpg"):
		cv2.imwrite(filename, self.image)


