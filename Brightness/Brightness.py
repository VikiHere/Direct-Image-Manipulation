from numpy import array
from PIL import Image


# Importing the Image into a 2-D Array
# ------------------------------------------- #

#storing the image into a veriable
imageBear = Image.open("183087.jpg")
#wb = 481, hb = 321
wb,hb = imageBear.size
imageArrayBear = array(imageBear)

imageGoat = Image.open("207056.jpg")
#wg = 512, hg = 512
wg,hg = imageGoat.size
imageArrayGoat = array(imageGoat)

# ------------------------------------------- #
#I = C*f(x,y) + B
    #C is any value
    #B is any value from 0 < B < 255

#Initializing the C and B 
C = 0.7
B = 100
newImageArrayBear = imageArrayBear
newImageArrayGoat = imageArrayGoat

for i in range (hb-1):
    for j in range (wb-1):
        temp = imageArrayBear[i][j]*C + B
        if (temp > 255):
            newImageArrayBear[i][j] = 255
        elif (temp < 0):
            newImageArrayBear[i][j] = 0
        else:
            newImageArrayBear[i][j] = C*imageArrayBear[i][j] + B

for i in range (hg-1):
    for j in range (wg-1):
        temp = imageArrayGoat[i][j]*C + B
        if (temp > 255):
            newImageArrayGoat[i][j] = 255
        elif (temp < 0):
            newImageArrayGoat[i][j] = 0
        else:
            newImageArrayGoat[i][j] = C*imageArrayGoat[i][j] + B
        

#Showing the new image with the applied C and B values
newImageArrayBear = Image.fromarray(newImageArrayBear,)
newImageArrayBear.save("new183087_C0_7B100.jpg")
newImageArrayBear.show()
newImageArrayGoat = Image.fromarray(newImageArrayGoat,)
newImageArrayGoat.save("newmotion01_512_C0_7B100.tiff")
newImageArrayGoat.show()
