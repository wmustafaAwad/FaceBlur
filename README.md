# FaceBlur
Detect Face and Blur it (single face expected)

Python Code using OpenCV and a bit of numpy to find faces in still images and blur them.

## Current version:
Takes as input the path of an image (in face_detect_tester.py) or a path full of images (in  face_detect.py) and outputs the same image(s) with the face of the person included blurred, if found.  
If many faces are there, only the largest face will be blurred. If no faces are there, nothing gets blurred. The output image is a BW version of the input Image.

## Later Versions:
The current version outputs a BW version of the images, with the blur using a 1-0 mask. Later versions should deal with RGB-colored images and use Gaussian mask on the blur effect.
Also, the same methodology will be applied to videos using FFmpeg. So, stay tuned.

## Tools used:
- OpenCV & Numpy in Python
- Pycharm 

## How to Use:
### face_detect.py (for multiple images):
#### - Download and run for testering.
#### - For personal use: 
1- Make sure the variable path has the correct path name leading to  where your images are located. 
2- Make sure the $cascPath$ variable leads to the file "haarcascade_frontalface_default.xml"
3- Changes the intensity to change the blur intensity.  (0-> No blur, with blur increasing as number increases.)
NB: The output files are written to the folder "Output Folder" in the same location of the .py file.

### face_detect_tester.py (for testing a single image):
1- Make sure the variable imagePath has the correct path name leading to where your imageis located. 
2- Make sure the $cascPath$ variable leads to the file "haarcascade_frontalface_default.xml"
3- Changes the intensity to change the blur intensity. (0-> No blur, with blur increasing as number increases.)
NB: Output files are not written to any folder, only displayed.

## Sample Outputs of current Version:
![Output](https://github.com/wmustafaAwad/FaceBlur/blob/master/Output%20Folder/Rami%20Malek.jpg) ![Input](https://github.com/wmustafaAwad/FaceBlur/blob/master/IMDB-Celeb-Faces/Rami%20Malek.jpg)
All other inputs are in the folder: 'IMDB Celeb Faces'. All other outputs are in the 'Output Folder'.
