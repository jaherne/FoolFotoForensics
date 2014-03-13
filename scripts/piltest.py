#!/usr/local/bin/python
from PIL import Image, ImageFilter
import argparse, os
import fff

# parse command line arguments
parser = argparse.ArgumentParser()
parser.add_argument("image", help="image you want to perform ELA on")
parser.add_argument("-v", "--verbose", help="verbose output", action="store_true")
parser.add_argument("-s", "--show", help="show images with default image viewer",
	action="store_true")
args = parser.parse_args()
qual = 75
scale = 15

 # load the original and convert to YCbCr
original = fff.open_image(args.image)
if (args.show):
	original.show()
if (args.verbose):
	print("Opening: " + args.image + " in YCbCr")

# load pixels from converted image into array
pixarr = original.load() 
if (args.verbose):
	print("Loading image into pixel array")

# save image at lower quality
original.save("images/test.jpg", quality=qual)
if (args.verbose):
	print("Saving at quality: " + str(qual))

# open worse quality image
new = fff.open_image("images/test.jpg")
newarr = new.load()
if (args.show):
	new.show()
if (args.verbose):
	print("Opening lower quality image")

# the important part
# absolute value original Y values - new Y values
# multiply everything by the set scale 
errArr = pixarr
errArr = fff.ela(pixarr, newarr, scale, original, "Y")
if(args.verbose):
	print("Performing ELA")
if (args.show):	
	new.show()

new.save("images/posttool.jpg", quality=100)
if (args.verbose):
	print("Saving ELA of image")

'''fuzzArr = pixarr
fuzzArr = fff.fuzzELA(pixarr, newarr, errArr, original, scale)
original.save("images/asdf.jpg", quality=100)
'''
# cleanup
os.remove("images/test.jpg")