#!/usr/bin/env python
from PIL import Image, ImageFilter
 
original = Image.open("images/books-edited.jpg") # load an image from the hard drive
changed = original.convert("YCbCr") # Convert from RGB to YCbCr
changed.show()
pixarr = changed.load() # load pixels from image into array

for j in range(changed.size[1]): # For every single pixel
	for i in range (changed.size[0]):
		#print(pixarr[i,j])l
		place=pixarr[i,j][1]
		holder=pixarr[i,j][2]
		#pixarr[i,j] = (0,place,holder) # Change the luminance
		#print(pixarr[i,j])

#changed.show() # will print it as dark

changed.save("images/test.jpg", quality=5)

new = Image.open("images/test.jpg").show() # Open image again with worse quality

# helpful documentation for this library @ http://effbot.org/imagingbook/image.htm
