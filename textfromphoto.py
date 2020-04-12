#I think this will be the most challenging part of the project. 
from PIL import Image
import pytesseract

#Need to accept photo as input.
class Photo():

	def __init__(self, image):
		self.data = Image.open(image)
	
	def resize(self, image):
		self.image = cv2.resize(warped, (1350, 1150))


#Need to find framework to read text from photo.




