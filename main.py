#Main will glue the pieces together when finished. 

import readimage as img
import dates

#Called by web app to take image as input and return read data as string
def output(image):
	return img.read(img.input(image))

days = {}

def gen_class(image):
	crop_size = int(image.shape[0]/7)
	top = 0
	bottom = crop_size
	for i in range(7):
		cropped = img.crop(image, top = top, bottom = bottom)
		text = img.read(cropped).split()
		#Use text to generate new class instance here
		print(text)
		top = bottom
		bottom = bottom + crop_size

#notes for tesseract
#config = r'--oem 3 --psm *'
#pytesseract.image_to_string(x, config=config)
#psm 3 (default) works best for Days
#psm 12 works best for Times

'''
***Transforming image notes:***
pts1 = np.float32([[points.item(0)+20,points.item(1)-20],[points.item(2)+20,points.item(3)+20],[points.item(4)-20,points.item(5)+20],[points.item(6)-20,points.item(7)-20]])
pts2 = np.float32([[2500,0],[2500,4000],[0,4000],[0,0]])
M = cv2.getPerspectiveTransform(pts1,pts2)
dst = cv2.warpPerspective(image,M,(2510,4000))

transCopy = dst.copy()
trans = dst.copy()
trans = img.grayscale(trans)
trans = img.edged(trans)
cnts = img.findContours(trans)
cnts = img.sortContours(cnts)
img.drawContours(transCopy, cnts)
img.write(transCopy)
'''
