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
mask_yellow = cv.inRange(hsv, (170,100,100), (180, 255, 255))

#Get the mask of the red and yellow value
mask_maroon = cv.inRange(hsv, (0,25,25), (10, 255, 255))

#Get the masl of the orange values
mask_orange = cv.inRange(hsv, (0,50,50), (25, 255, 255))


#Get the mask of the red and yellow value
mask_green = cv.inRange(hsv, (35,100,100), (77, 255, 255))

#Get the mask of the red and yellow value
mask_brown = cv.inRange(hsv, (78,100,100), (99, 255, 255))

#Get the mask of the red and yellow value
mask_green_brown = cv.inRange(hsv, (100,100,100), (124, 255, 255))


#combines all the colors needed
mask_combination = cv.bitwise_or(mask_red, mask_yellow, mask_maroon)


mask_combinationOpp= cv.bitwise_or(mask_green, mask_green_brown, mask_brown)

#keeps only the red color
imask_red = mask_red>0
red = np.zeros_like(img, np.uint8)
red[imask_red] = img[imask_red]

#keeps only the yellowcolor
imask_yellow = mask_yellow>0
yellow = np.zeros_like(img, np.uint8)
yellow[imask_yellow] = img[imask_yellow]

#keeps only the maroon color
imask_maroon = mask_maroon>0
maroon = np.zeros_like(img, np.uint8)
maroon[imask_maroon] = img[imask_maroon]

#combines both colors
imask_combine = mask_combination>0
combine = np.zeros_like(img, np.uint8)
combine[imask_combine] = img[imask_combine]



#keeps only the green
imask_green = mask_green>0
green = np.zeros_like(img, np.uint8)
green[imask_green] = img[imask_green]

#keeps only the brown
imask_brown = mask_brown>0
brown = np.zeros_like(img, np.uint8)
brown[imask_brown] = img[imask_brown]

#keeps only the brown
imask_green_brown= mask_green_brown>0
green_brown = np.zeros_like(img, np.uint8)
green_brown[imask_green_brown] = img[imask_green_brown]

#keeps only the orange color
imask_orange = mask_orange>0
orange = np.zeros_like(img, np.uint8)
orange[imask_maroon] = img[imask_orange]

#combines both colors
imask_combineOpp = mask_combinationOpp>0
combineOpp = np.zeros_like(img, np.uint8)
combineOpp[imask_combineOpp] = img[imask_combineOpp]


#erosion function
kernel = np.ones((5,5),np.uint8)
erosion = cv.erode(combine,kernel,iterations = 2)

#dilation fucntionq
kernel = np.ones((5,5),np.uint8)
dilation = cv.dilate(erosion,kernel,iterations = 2)


#print out the red image and hte original ima0ge side by side
cv.imshow("original", img)
cv.imshow("red", red)
cv.imshow("maroon", maroon)
cv.imshow("Combined", combine)
# cv.imshow("CombinedOpp", combineOpp)
cv.imshow("erosion", erosion)
cv.imshow("dilation", dilation)
cv.waitKey(0)
cv.destroyAllWindows()