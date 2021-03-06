#Main will glue the pieces together when finished. 

import readimage as img
import dates

#Called by web app to take image as input and return read data as string
def output(image):
    return img.read(img.input(image))

#Transform image based on calendar outline for ease of splitting information into individual days
def transform_image(image):
    copy = image.copy()
    image = img.prep_for_contours(image)
    contours = img.do_contours(image)
    print(contours)
    return img.transform(copy, contours)

#Generates an array of Date objects to hold the upcoming Date instances
days = [dates.Date() for i in range(7)]

#Crops calendar into individual days and populates Date instances with the information
def gen_class(image):
    crop_size = int(image.shape[0]/7)
    top = 0
    bottom = crop_size
    for i in range(len(days)):
        cropped = img.crop(image, top = top, bottom = bottom)
        text = img.read(cropped).split()
        days[i].assignDay(text)
        days[i].assignTime(text)
        days[i].clean()
        days[i].assignBlock()
        #print(days[i].toString())
        top = bottom
        bottom = bottom + crop_size

#def main(image):
def main():
    image = img.image('img.JPG') #Remove after testing
    image = transform_image(image)
    img.write(image)
    gen_class(image)
    for i in range(len(days)):
        print(days[i].toString())

''' To Do:
Begin interfacing with Google Calendar
'''
