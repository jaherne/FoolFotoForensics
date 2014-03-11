# Fool Foto Forensics module
# Code for basic image parsing and ELA 

# Imports:
from PIL import Image, ImageFilter
import os

# openImage
# Opens an image and converts to YCbCr
# Parameters: 
# 	file: the filename of the image to open
# Returns:
#	image: the image as a PIL object

def openImage(file):
	image = Image.open(file).convert("YCbCr")
	return image

# ela
# Performs ELA on a specified value
# Takes the absolute value of the original value
# minus the resaved value. These values are then 
# stored and returned in a new array, which can be
# saved or displayed as desired. 
# Parameters:
# 	origArr: The pixel array of the original image
#	newArr: The pixel array of the resaved image
#	scale: The magnification amount 
#	image: The PIL image object
#	value: Y, Cb, or Cr to do ela on. Defaults to Y
# Returns: 
#	errArr: The pixel array of the error analyis

def ela(origArr, newArr, scale, image, value = "Y"):
	if value != "Y" and value != "Cb" and value != "Cr":
		return 1 # Value is not specified correctly

	errArr = newArr
	for y in range(image.size[1]):
		for x in range (image.size[0]):
			if value == "Y":
				Yerr = abs(origArr[x,y][0] - newArr[x,y][0])
				#print Yerr + "\n"
				Cerr = origArr[x,y][1]
				Cberr = origArr[x,y][2]
			if value == "Cb":
				Yerr = origArr[x,y][0]
				Cerr = abs(origArr[x,y][1] - newArr[x,y][1])
				Cberr = origArr[x,y][2]
			if value == "Cr":
				Yerr = origArr[x,y][0]
				Cerr = origArr[x,y][1]
				Cberr = abs(origArr[x,y][2] - newArr[x,y][2])
			errArr[x,y] = (Yerr * scale, Cerr * scale, Cberr * scale)

	return errArr