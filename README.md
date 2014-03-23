FoolFotoForensics
=================

Purpose of the tool:   
Prevent Error Level Analysis from returning useful data when analyzing a given image. An example of the tool in use can be seen here: http://imgur.com/a/Kcfk3

Install Steps:  
1.	Install Pillow "pip install pillow"  
2.	Install libjpeg-dev package

Current Status:  
Quicktest.py reads in an image and converts to YCbCr. It is then saved at a lower quality. A third image is created that consists of the delta between the Y values, multiplied by a hardcoded scale. Next, each pixel is analyzed for the difference between the initial and resaved values. If it exceeds a certain hardcoded amount, the original pixel is changed to the resaved pixel.  

Piltest.py performs a similar function, but without the fuzzing at the end. Its purpose is to analyze the already changed image, and show that ELA will no longer work. 

To Do list:   
1.  Integrate ImageChops  
2.  Cleanup second ELA, currently just PoC in fuzzELA.py  
3.  Implement new system for deciding what pixels are fuzzed  
4.  Cleanup fuzzELA.py of testing code  
5.  Add more flags per written plan  
6.  Improve documentation  
7.	Test lots and lots  


Completed:  
~~1.    Build out script functionality (command arguments, etc)~~      
~~2.	Determine error levels of given image~~  
~~3.	Isolate areas with high error levels~~  
~~4.	Change brightness such that the error level is minimized~~  
~~5.	Save back to original image.~~  
~~6.  Refactor code with functions~~  
~~7.  Combine the two scripts into a single file~~  
