FoolFotoForensics
=================

Purpose of the tool:   
Prevent Error Level Analysis from returning useful data when analyzing a given image. 

Install Steps:  
1.	Install Pillow "pip install pillow"  
2.	Install libjpeg-dev package

Current Status:  
Script takes the given image and converts it into YCbCr format. The brightness levels can be changed before it is saved at a lower quality than the original image. 

Next Steps:   
1.	Build out script functionality (command arguments, etc)
2.	Determine error levels of given image  
3.	Isolate areas with high error levels  
4.	Change brightness such that the error level is minimized  
5.	Save back to original iimage.
