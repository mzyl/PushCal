#Main will glue the pieces together when finished. 

import readimage as img

#Called by web app to take image as input and return read data as string
def output(image):
	return img.read(img.input(image))

#Return separate image containing the space of days
def splitDays(image):
	return image[0:, 0:int(image.shape[1]/2)]

#Return separate image containing the space of times
def splitTimes(image):
	return image[0:, int(image.shape[1]/2):]

#notes for tesseract
#config = r'--oem 3 --psm *'
#pytesseract.image_to_string(x, config=config)
#psm 3 (default) works best for Days
#psm 12 works best for Times

