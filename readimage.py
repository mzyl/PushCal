import cv2
import imutils
import pytesseract
import numpy as np

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

#Transform points evaluation
def point_eval(point):
    if point < 1000:
        return 0
    elif point < 3000:
        return 2500
    else:
        return 4000

#Transform perspective
#***** Very static setup, needs to be dynamic *****# 
#**    Is more dynamic, but feels a bit crude
def transform(image, points):
    #Points with padding for drawing contours
    #pts1 = np.float32([[points.item(0)+20,points.item(1)-20],[points.item(2)+20,points.item(3)+20],[points.item(4)-20,points.item(5)+20],[points.item(6)-20,points.item(7)-20]])
    pts1 = np.float32([[points.item(0),points.item(1)],[points.item(2),points.item(3)],[points.item(4),points.item(5)],[points.item(6),points.item(7)]])
    #pts2 = np.float32([[2500,0],[2500,4000],[0,4000],[0,0]])
    #pts2 = np.float32([[0,0],[0,4000],[2500,4000],[2500,0]])
    pts2 = np.float32([[point_eval(points.item(0)),point_eval(points.item(1))],[point_eval(points.item(2)),point_eval(points.item(3))],[point_eval(points.item(4)),point_eval(points.item(5))],[point_eval(points.item(6)),point_eval(points.item(7))]])
    M = cv2.getPerspectiveTransform(pts1, pts2)
    return cv2.warpPerspective(image, M, (2500,4000))

'''Contour/Line mapping functions'''

#Find contours
def find_contours(image):
    return cv2.findContours(image, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)

#Sort contours
def sort_contours(contours):
    contours = imutils.grab_contours(contours)
    return sorted(contours, key = cv2.contourArea, reverse = True)[:5]

#Get outline of calendar via contours without drawing
def get_outline(contours):
    for c in contours:
        peri = cv2.arcLength(c, True)
        approx = cv2.approxPolyDP(c, 0.02 * peri, True)
        if len(approx) == 4:
            return approx

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

#Returns edged image from input image, ready to find calendar outline
def prep_for_contours(image):
    image = grayscale(image)
    image = noise_removal(image)
    return edged(image)

#Use contours to return calendar outline
def do_contours(image):
    contours = find_contours(image)
    contours = sort_contours(contours)
    return get_outline(contours)

