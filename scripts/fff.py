# Fool Foto Forensics module
# Code for basic image parsing and ELA

# Imports:
from PIL import Image, ImageFilter
import os

# open_image
# Opens an image and converts to YCbCr
# Parameters:
#   file: the filename of the image to open
# Returns:
#   image: the image as a PIL object


def open_image(file):
    image = Image.open(file).convert("YCbCr")
    return image

# ela
# Performs ELA on a specified value
# Takes the absolute value of the original value
# minus the resaved value. These values are then
# stored and returned in a new array, which can be
# saved or displayed as desired.
# Parameters:
#   origArr: The pixel array of the original image
#   newArr: The pixel array of the resaved image
#   scale: The magnification amount
#   dimensions: The x and y size of the image
#   value: Y, Cb, or Cr to do ela on. Defaults to Y
# Returns:
#   errArr: The pixel array of the error analyis


def ela(origArr, newArr, scale, dimensions, value="Y"):
    if value != "Y" and value != "Cb" and value != "Cr":
        return 1  # Value is not specified correctly

    width = dimensions[0]
    height = dimensions[1]
    errArr = newArr

    for y in range(height):
        for x in range(width):
            if value == "Y":
                Yerr = abs(origArr[x, y][0] - newArr[x, y][0])
                Cerr = origArr[x, y][1]
                Cberr = origArr[x, y][2]
            if value == "Cb":
                Yerr = origArr[x, y][0]
                Cerr = abs(origArr[x, y][1] - newArr[x, y][1])
                Cberr = origArr[x, y][2]
            if value == "Cr":
                Yerr = origArr[x, y][0]
                Cerr = origArr[x, y][1]
                Cberr = abs(origArr[x, y][2] - newArr[x, y][2])
            errArr[x, y] = (Yerr * scale, Cerr * scale, Cberr * scale)

    return errArr

# fuzz
# Given the error levels, this will fuzz the original
# pixels to the resaved values. Requires fff.ela to
# have been run already.
# Parameters:
#   origArr: The pixel array of the original image
#   newArr: The pixel array of the resaved image
#   errArr: The pixel array of the error analysis
#   scale: The magnification amount
#   dimensions: The x and y size of the image
# Returns:
#   fuzzArr: The original picture's pixel array with fuzzing


def fuzz(origArr, newArr, errArr, scale, dimensions):
    fuzzArr = origArr
    difflist = []
    width = dimensions[0]
    height = dimensions[1]

    for y in range(height):
        for x in range(width):
            diff = (
                (errArr[x, y][0] + errArr[x, y][1] + errArr[x, y][2]) / scale)
            if diff >= 40:
                fuzzArr[x, y] = (
                    newArr[x, y][0], newArr[x, y][1], newArr[x, y][2])

    return fuzzArr
