from PIL import Image, ImageFilter
 
original = Image.open("images/books-edited.jpg") # load an image from the hard drive
changed = original.convert("L") # Convert from RGB to YCbCr
pixarr = changed.load() # load pixels from image into array

#for j in range(changed.size[1]):
	#for i in range (changed.size[0]):
		#print(pixarr[i,j])
		#tup = pixarr[i,j]
		#pixarr[i,j] = (255,tup[1],tup[2]) 

changed.show() # will print just in greyscale

# helpful documentation for this library @ http://effbot.org/imagingbook/image.htm
