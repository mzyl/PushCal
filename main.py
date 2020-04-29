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
