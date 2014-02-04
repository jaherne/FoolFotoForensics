from PIL import Image, ImageFilter
 
original = Image.open("images/books-edited.jpg") # load an image from the hard drive
changed = original.convert("L") # Convert from RGB to YCbCr
pixarr = changed.load() # load pixels from image into array

for j in range(changed.size[1]): # For every single pixel
	for i in range (changed.size[0]):
		#print(pixarr[i,j])
		pixarr[i,j] = 125 # Change the pixel to grey
		#print(pixarr[i,j])

changed.show() # will print just grey

# helpful documentation for this library @ http://effbot.org/imagingbook/image.htm
