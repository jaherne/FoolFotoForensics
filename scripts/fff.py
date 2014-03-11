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

