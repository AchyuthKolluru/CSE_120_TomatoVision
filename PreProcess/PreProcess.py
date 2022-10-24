from distutils.errors import LibError
from math import comb
from pickletools import uint8
import numpy as np
import cv2 as cv

img = cv.imread("IMG_20220914_171704.jpg")
hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
h,s,v = cv.split(hsv)

#Gets the mask of the red value
mask_red = cv.inRange(hsv, (0,100,100), (10, 255, 255))

#Get the mask of the red and yellow value
mask_yellow = cv.inRange(hsv, (170,100,100), (25, 255, 255))

#Get the mask of the red and yellow value
mask_maroon = cv.inRange(hsv, (0,120,120), (50, 255, 255))

#Get the mask of the orange values
mask_orange = cv.inRange(hsv, (0,50,50), (25, 255, 255))


#Get the mask of the red and yellow value
mask_green = cv.inRange(hsv, (35,100,100), (77, 255, 255))

#Get the mask of the red and yellow value
mask_brown = cv.inRange(hsv, (78,100,100), (99, 255, 255))

#Get the mask of the red and yellow value
mask_green_brown = cv.inRange(hsv, (100,100,100), (124, 255, 255))


# #combines all the colors needed
# mask_combination = cv.bitwise_xor(mask_red, mask_yellow, mask_maroon)


mask_combinationOpp= cv.bitwise_and(mask_green, mask_green_brown, mask_brown, mask_orange)

# #keeps only the red color
def red_mask(img):
    imask_red = mask_red>0
    red = np.zeros_like(img, np.uint8)
    red[imask_red] = img[imask_red]
    return red

# #keeps only the yellowcolor
def orange_mask(img):
    imask_yellow = mask_yellow>0
    yellow = np.zeros_like(img, np.uint8)
    yellow[imask_yellow] = img[imask_yellow]
    return yellow

# #keeps only the maroon color
def maroon_mask(img):
    imask_maroon = mask_maroon>0
    maroon = np.zeros_like(img, np.uint8)
    maroon[imask_maroon] = img[imask_maroon]
    return maroon

# #combines both colors
# def combination_mask(img):
#     imask_combine = mask_combination>0
#     combine = np.zeros_like(img, np.uint8)
#     combine[imask_combine] = img[imask_combine]
#     return combine



#keeps only the green
def green_mask(img):
    imask_green = mask_green>0
    green = np.zeros_like(img, np.uint8)
    green[imask_green] = img[imask_green]
    return green

#keeps only the brown
def brown_mask(img):
    imask_brown = mask_brown>0
    brown = np.zeros_like(img, np.uint8)
    brown[imask_brown] = img[imask_brown]
    return brown

#keeps only the brown
def green_brown_mask(img):
    imask_green_brown= mask_green_brown>0
    green_brown = np.zeros_like(img, np.uint8)
    green_brown[imask_green_brown] = img[imask_green_brown]
    return green_brown_mask

# #keeps only the orange color
def orange_mask(img):
    imask_orange = mask_orange>0
    orange = np.zeros_like(img, np.uint8)
    orange[imask_orange] = img[imask_orange]
    return orange

# #combines both colors
def combineOpp(img):
    imask_combineOpp = mask_combinationOpp>0
    combineOpp = np.zeros_like(img, np.uint8)
    combineOpp[imask_combineOpp] = img[imask_combineOpp]
    return combineOpp


#erosion function
def EROSION(img):
    kernel = np.ones((7,7),np.uint8)
    erosion = cv.erode(img,kernel,iterations = 2)
    return erosion

#blur 
def BLUR(img):
    blur = cv.blur(img,(10,10))
    return blur

#dilation fucntion
def DILATION(img):
    kernel = np.ones((5,5),np.uint8)
    dilation = cv.dilate(img,kernel,iterations = 2)
    return dilation

def EDGE(img):
    edges = cv.Canny(img, 100, 200)
    return edges


#print out the red image and hte original ima0ge side by side
cv.imshow("original", img)
# cv.imshow("red", red_mask(img))
# cv.imshow("orange", orange_mask(img))
cv.imshow("maroon", BLUR(maroon_mask(img)))
# cv.imshow("Combined", combination_mask(img))
# cv.imshow("erosion", EROSION(maroon_mask(img)))
cv.imshow("blur", BLUR(img))
cv.imshow("edges", EDGE(EROSION(BLUR(maroon_mask(img)))))
# cv.imshow("dilation", DILATION(maroon_mask(img)))
cv.waitKey(0)
cv.destroyAllWindows()