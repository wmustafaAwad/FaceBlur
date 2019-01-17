import cv2
import sys
import numpy as np

'''
Goal: Write a code to get as an input an image with a face, then return the same image* with the face blurred.
*for now, the returned image is BW for demonstration purposes only.

'''
#----------- Function Definitions -----------#
def apply_gaussian_mask2(Image, x, y, w, h, intensity):
    # dependencies: cv2, numpy as np
    '''
    :param Image: Input image read from cv2 before input
    :param x: x coordinate of face (left most corner, not centre)
    :param y: y coordinate of face (highest corner, not centre)
    :param w: width of rectangle encapsulating  face
    :param h: height of rectangle encapsulating  face
    :param intensity: Blur intensity. 0-> no blur.
        #8 blur value is good for hiding faces but still showing general characteristics of face.
    :return: Grayscale image to which the face-blur is applied.

    :Future enhancemenets: Gaussian mask after blur to avoid blurred rectangle. Also output RGB not grayscale (apply blur to each channel)
    '''
    # Change input to BW (remove and deal with 3D matrix for RGB):
    Image = cv2.cvtColor(Image, cv2.COLOR_BGR2GRAY)
    Imsize = Image.shape

    # Center of face positions for x,y coords
    CenterPosx = x + int(w / 2)
    CenterPosy = y + int(h / 2)

    # Create image to overlay
    cropped = Image[x:x + w, y:y + h]
    toblur = np.zeros(Imsize)
    toblur[x:x + w, y:y + h] = cropped
    overlay = cv2.GaussianBlur(cv2.blur(cropped, (5, 5)), (25, 25), intensity)
    overlaid = Image
    overlaid[x:x + w, y:y + h] = overlay
    return overlaid

def get_face_with_largest_area(faces):
    '''

    :param faces: array where each row is equal to [x,y,width,height] of a detected face. Each row represents a face.
    :return: the row for the face with larges area (width*height) to blur only one face.
    '''
    cntr = 0
    max = 0
    index = 0
    for (x, y, w, h) in faces:
        if (w * h > max):
            index = cntr
            max = w * h
        cntr += 1
    return faces[index]

#----------- EOf Function Definitions--------#
#--%                                       %--#
#-----%                                 %-----#
#--------%                           %--------#
#--------%                           %--------#
#-----%                                 %-----#
#--%                                       %--#
#-------------- Variables Def ----------------#
imagePath = "IMDB-Celeb-Faces\Rami Malek.jpg" #sys.argv[0]
cascPath = "haarcascade_frontalface_default.xml" #sys.argv[1]
intensity= 8#sys.argv[2]
faceCascade = cv2.CascadeClassifier(cascPath)
#------------- EOf Variables Def -------------#


#Read image and convert to BW:
image = cv2.imread(imagePath)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Detect faces in the image
faces = faceCascade.detectMultiScale(
    gray,
    scaleFactor=1.1,
    minNeighbors=5,
    minSize=(30, 30),
    flags = cv2.CASCADE_SCALE_IMAGE
)


#Blur faces in overlay image:
overlay=cv2.GaussianBlur(cv2.blur(image,(3*intensity,3*intensity)),(5,5),intensity*200)

#Get largest object detected as face only:
    #so that if other objects are detected as a face they will be removed.
[facey,facex,facew,faceh]=get_face_with_largest_area(faces)

output=apply_gaussian_mask2(image,facex,facey,facew,faceh,8)
cv2.imshow("Blurred Face", output)


cv2.waitKey(0)
