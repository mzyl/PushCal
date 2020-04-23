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

	#Pull text from image
	def read(self):
		return pytesseract.image_to_string(self.image)

	#Write image to file
	def write(self, filename = "modified.jpg"):
		cv2.imwrite(filename, self.image)

	#Crop image to spec
	def crop(self, left = 0, right = 0, top = 0, bottom = 0):
		self.image = self.image[0:, 0:int(self.image.shape[1]/2)]

	#Resize image
	def resize(self, height):
		self.image = imutils.resize(self.image, height = height)
	
	#Grayscale
	def gray(self):
		self.image = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)

	#Gaussian Blur
	def guassian(self):
		self.image = cv2.GaussianBlur(self.image, (5, 5), 0)

	#Creates an edged image for easier OCR
	def edged(self):
		self.image = cv2.Canny(self.image, 75, 200)

	#Noise removal
	def removeNoise(self):
		self.image = cv2.medianBlur(self.image, 5)

	#Thresholding - Not sure what this does yet -- Errors anyway
	def thresholding(self):
		self.image = cv2.threshold(self.image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]


