#!/usr/bin/env python
from PIL import Image, ImageFilter
import argparse, os

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
original = Image.open(args.image) 
if (args.verbose):
	print("Opening: " + args.image)
changed = original.convert("YCbCr")
if (args.verbose):
	print("Converting to YCbCr")
if (args.show):
	original.show()

# load pixels from converted image into array
pixarr = changed.load() 
if (args.verbose):
	print("Loading image into pixel array")

# save image at lower quality
changed.save("images/test.jpg", quality=qual)
if (args.verbose):
	print("Saving at quality: " + str(qual))

# open worse quality image
new = Image.open("images/test.jpg").convert("YCbCr") 
newarr = new.load()
if (args.show):
	new.show()

# the important part
# absolute value original Y values - new Y values
# multiply everything by the set scale 
err = newarr
for n in range(new.size[1]):
	for m in range (new.size[0]):
		a = abs(pixarr[m,n][0] - newarr[m,n][0])
		b = pixarr[m,n][1]#abs(pixarr[m,n][1] - newarr[m,n][1])
		c = pixarr[m,n][2]#abs(pixarr[m,n][2] - newarr[m,n][2])
		#print(pixarr[m,n])		
		#print(newarr[m,n])
		err[m,n] = (a*scale, b*scale, c*scale)
		#print(str(err[m,n]))
	
if (args.show):	
	new.show()

# cleanup
os.remove("images/test.jpg")