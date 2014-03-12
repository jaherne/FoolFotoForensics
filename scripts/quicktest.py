#!/usr/local/bin/python
from PIL import Image, ImageFilter
import argparse, os
import fff

original = fff.openImage("images/books-edited.jpg")
fuzz = fff.openImage("images/books-edited.jpg")
final = fff.openImage("images/books-edited.jpg")

origArr = original.load()
original.save("images/test.jpg", quality=75)
new = fff.openImage("images/test.jpg")
ela = fff.openImage("images/test.jpg")
newArr = new.load()

elaArr = ela.load()
fuzzArr = fuzz.load()
finalArr = final.load()

elaArr = fff.ela(origArr, elaArr, 15, original)
ela.show()
ela.save("images/pretool.jpg")

fuzzArr = fff.fuzz(fuzzArr, newArr, elaArr, original, 15)


fuzz.save("images/books-posttool.jpg")
os.remove("images/test.jpg")