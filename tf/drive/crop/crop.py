from openpyxl import Workbook,load_workbook
from pixel_selector import Selector
import numpy as np
import cv2 as cv
img_dir= r"C:\Users\hasan.uzunova\Desktop"
img_path= r"C:\Users\hasan.uzunova\Desktop\tumfoto.png"
selector = Selector(img_dir)


selector.find_images()
selector.load_stats()

selector.img_path = img_path
selector.image_handler()
these_coords = selector.save_stats()
xcoord=[]
ycoord=[]
for i in range(0,len(these_coords)):
    xcoord.append(these_coords[i][0])
    ycoord.append(these_coords[i][1])

# Importing Image class from PIL module
from PIL import Image

# Opens a image in RGB mode
im = Image.open(r"C:\Users\hasan.uzunova\Desktop\tumfoto.png")


# Setting the points for cropped image
left = min(xcoord)
top = min(ycoord)
right = max(xcoord)
bottom = max(ycoord)

 #Cropped image of above dimension
# (It will not change original image)
#im1 = im.crop((left, top, right, bottom))

# Shows the image in image viewer
#im1.show()
#cv.imwrite("tumfoto.png",im)

im1 = im.crop((left, top, right, bottom))
im1.save('tumfoto.png')
im1.show()