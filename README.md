FoolFotoForensics
=================

Purpose of the tool:   
Prevent Error Level Analysis from returning useful data when analyzing a given image. An example of the tool in use can be seen here: http://imgur.com/a/Kcfk3

Install Steps:  
1.	Install Pillow "pip install pillow"  
2.	Install libjpeg-dev package

Current Status:  
fuzzELA, when given a file, will perform an Error Level Analysis (ELA) on the image. It will then attempt to fuzz the image, by converting pixels with higher error levels to the resaved value. If chosen, a second ELA can be performed with the -g flag, so that a comparison of pre and post fuzzing can be easily seen. 

To Do list:   
1.  Integrate ImageChops  
2.  Cleanup second ELA, currently just PoC in fuzzELA.py  
3.  Implement new system for deciding what pixels are fuzzed  
4.  Cleanup fuzzELA.py of testing code  
5.  Add more flags per written plan  
6.  Add maximum verbosity
7.  Improve documentation  
8.	Test lots and lots  


Completed:  
~~1.    Build out script functionality (command arguments, etc)~~      
~~2.	Determine error levels of given image~~  
~~3.	Isolate areas with high error levels~~  
~~4.	Change brightness such that the error level is minimized~~  
~~5.	Save back to original image.~~  
~~6.    Refactor code with functions~~  
~~7.    Combine the two scripts into a single file~~  
