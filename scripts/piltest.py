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

 
original = Image.open(args.image) # load an image
if (args.verbose):
	print("Opening: " + args.image)
changed = original.convert("YCbCr") # Convert from RGB to YCbCr
if (args.verbose):
	print("Converting to YCbCr")
if (args.show):
	original.show()

pixarr = changed.load() # load pixels from image into array
if (args.verbose):
	print("Loading image into pixel array")

for j in range(changed.size[1]): # For every single pixel
	for i in range (changed.size[0]):
		#print(pixarr[i,j])
		place=pixarr[i,j][1]
		holder=pixarr[i,j][2]
		#pixarr[i,j] = (0,place,holder) # Change the luminance
		#print(pixarr[i,j])

changed.save("images/test.jpg", quality=qual)
if (args.verbose):
	print("Saving at quality: " + str(qual))

new = Image.open("images/test.jpg").convert("YCbCr") # Open image again with worse quality
newarr = new.load()
if (args.show):
	new.show()

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
		
new.show()

os.remove("images/test.jpg") # cleanup
# helpful documentation for this library @ http://effbot.org/imagingbook/image.htm
