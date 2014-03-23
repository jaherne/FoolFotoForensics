#!/usr/local/bin/python
'''
    fuzzELA.py
'''

# Imports
from PIL import Image, ImageFilter
import argparse
import os
import fff

# Parse command line Arguments
parser = argparse.ArgumentParser()
#parser.add_argument("image", help="Image you want to analyze")
parser.add_argument("-v", "--verbose", help="verbose output", action="store_true")
parser.add_argument("-g", "--graphics", help="show ELA and post fuzzing ELA", action="store_true")
parser.add_argument("-q", "--quality", help="Quality level of resaved image. Lower quality means larger error levels. Defaults to 75.", default=75)
parser.add_argument("-s", "--scale", help="Amount to boost error levels by. Larger scale means larger error levels. Defaults to 15.", default=15)
'''
    TODO:
    Add remaining command line arguments
    Uncomment add_argument(image)
'''
args = parser.parse_args()

# TESTING ONLY:
image = "images/books-edited.jpg"

# Variables
tmp_image_location = "images/worse.jpg"  # Where to store the low quality image

# Open the image for processing
original = fff.open_image(image)
fuzzed = fff.open_image(image)
orig_pixels = original.load()
fuzz_pixels = fuzzed.load()
dimensions = [original.size[0], original.size[1]]

# Resave image for ELA comparison
original.save(tmp_image_location, quality=args.quality)
worse = fff.open_image(tmp_image_location)
error = fff.open_image(tmp_image_location)
worse_pixels = worse.load()
err_pixels = error.load()

# ELA of unedited image
err_pixels = fff.ela(orig_pixels, err_pixels, args.scale, dimensions)

if (args.graphics):
    error.show()

# Fuzz the image
fuzz_pixels = fff.fuzz(fuzz_pixels, worse_pixels, err_pixels, args.scale, dimensions)
fuzzed.save("images/books-posttool.jpg", quality=100)

if (args.graphics):
    fuzzed.save("images/worse2.jpg", quality=args.quality)
    error2 = fff.open_image("images/worse2.jpg")
    err2_pixels = error2.load()
    err2_pixels = fff.ela(fuzz_pixels, err2_pixels, args.scale, dimensions)
    error2.show()
    os.remove("images/worse2.jpg")


# End of execution cleanup
os.remove(tmp_image_location)
