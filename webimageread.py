from PIL import Image
import pytesseract

def image(filename):
	return pytesseract.image_to_string(Image.open(filename))

