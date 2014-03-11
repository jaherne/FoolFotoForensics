FoolFotoForensics
=================

Purpose of the tool:   
Prevent Error Level Analysis from returning useful data when analyzing a given image. 

Install Steps:  
1.	Install Pillow "pip install pillow"  
2.	Install libjpeg-dev package

Current Status:  
Script reads in an image and converts to YCbCr. It is then saved at a lower quality. A third image is created that consists of the delta between the Y values, multiplied by a hardcoded scale. 

Next Steps:   
~~1.  Build out script functionality (command arguments, etc)~~  
2.	Refactor code with functions  
3.	Determine error levels of given image  
4.	Isolate areas with high error levels  
5.	Change brightness such that the error level is minimized  
6.	Save back to original iimage.
