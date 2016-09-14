import cv2
import glob
import os

Richtung=1

if Richtung==0:
    R="front"
if Richtung==1:
    R="right"
if Richtung==2:
    R="left"
if Richtung==3:
    R="no"

TarFolder= Richtung.__str__() + "_Flipped"
os.mkdir(TarFolder)

filenames = glob.glob(Richtung.__str__() + '/*.png')

for x in range(0,len(filenames),1):
        name = filenames[x]
        picture=cv2.imread(name, 1)
        #resized = cv2.resize(picture, (256, 256))

        #Scales input image with 620x360 mit scale factor /2.5
        #resized=cv2.resize(picture, (248,144));
        flipped=cv2.flip(picture,1)
        cv2.imwrite(TarFolder + "/" + R + "%d.png" % x, flipped)
exit()
