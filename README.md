FoolFotoForensics
=================

Purpose of the tool:   
Prevent Error Level Analysis from returning useful data when analyzing a given image. 

Install Steps:  
1.	Install Pillow "pip install pillow"  
2.	Install libjpeg-dev package

Current Status:  
Quicktest.py reads in an image and converts to YCbCr. It is then saved at a lower quality. A third image is created that consists of the delta between the Y values, multiplied by a hardcoded scale. Next, each pixel is analyzed for the difference between the initial and resaved values. If it exceeds a certain hardcoded amount, the original pixel is changed to the resaved pixel.  

Piltest.py performs a similar function, but without the fuzzing at the end. Its purpose is to analyze the already changed image, and show that ELA will no longer work. 

Next Steps:    
1.	Refactor code with functions  (IN PROGRESS)  
2.	Combine the two scripts into a single file  
3.  Improve documentation  
4.	Test lots and lots


Completed:  
~~1.  Build out script functionality (command arguments, etc)~~      
~~2.	Determine error levels of given image~~  
~~3.	Isolate areas with high error levels~~  
~~4.	Change brightness such that the error level is minimized~~  
~~5.	Save back to original iimage.~~
