from numpy import array
from PIL import Image

# Importing the Image into a 2-D Array
# ------------------------------------------- #

#storing the image into a veriable
imageBridge = Image.open("bridge.png")
#wb = 534, hb = 340
wb,hb = imageBridge.size
imageArrayBridge = array(imageBridge)

imageFish = Image.open("fish.png")
#wb = 534, hb = 340
wf,hf = imageFish.size
imageArrayFish = array(imageFish)

imageMask = Image.open("mask.png")
#wb = 534, hb = 340
wm,hm = imageMask.size
imageArrayMask = array(imageMask)

# ------------------------------------------- #
#Using 3 images, A, B, and M apply the following
#   Image c =   A when M > 0
#               B when M = 0

#print(imageArrayMask)


tempImageArray = imageArrayMask
newImageArray = imageArrayBridge
newImageArrayPic = newImageArray



#use shape
#keep names like proper humans do
for i in range (hm-1):
    for j in range (wm-1):
        if (tempImageArray[i][j] > 0 ):
            newImageArray[i][j] = imageArrayFish[i][j]
        elif (tempImageArray[i][j] == 0):
            newImageArray[i][j] = imageArrayBridge[i][j]

#print(newImageArray)
#print(type(newImageArray))

newImageArrayPic = Image.fromarray(newImageArray,)
newImageArrayPic.save("newImageMasked.jpg")
newImageArrayPic.show()