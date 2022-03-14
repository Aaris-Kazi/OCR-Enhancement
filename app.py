import cv2 as cv
from urllib.request import urlopen
import numpy as np
req = urlopen("https://pyimagesearch.com/wp-content/uploads/2015/01/opencv_logo.png")
arr = np.asarray(bytearray(req.read()), dtype=np.uint8)
img = cv.imdecode(arr, cv.IMREAD_COLOR) # 'Load it as it is'

cv.imshow('lalala', img)
if cv.waitKey() & 0xff == 27: 
    quit()