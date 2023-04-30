# from tkinter import *
from PIL import Image
from banners import title


# Opening Image as an object
Img = Image.open("trippycode.jpeg")
# Getting the filename of image
print("Filename : ",Img.filename)
# Getting the format of image
print("Format : ",Img.format)
# Getting the mode of image
print("Mode : ",Img.mode)
# Getting the size of image
print("Size : ",Img.size)
# Getting only the width of image
print("Width : ",Img.width)
# Getting only the height of image
print("Height : ",Img.height)
# Getting the color palette of image
print("Image Palette : ",Img.palette)
# Getting the info about image
print("Image Info : ",Img.info)
# Closing Image object
Img.close()