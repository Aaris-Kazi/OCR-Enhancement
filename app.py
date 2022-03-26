# import cv2 as cv
# from urllib.request import urlopen
# import numpy as np
# req = urlopen("https://pyimagesearch.com/wp-content/uploads/2015/01/opencv_logo.png")
# req = urlopen("https://raw.githubusercontent.com/Aaris-Kazi/DIsease-Prediction-Online/main/static/img/19801.jpg")
# arr = np.asarray(bytearray(req.read()), dtype=np.uint8)
# img = cv.imdecode(arr, cv.IMREAD_COLOR) # 'Load it as it is'
# img = cv.resize(img, (300,300))
# cv.imshow('lalala', img)
# if cv.waitKey() & 0xff == 27: 
#     quit()

from cv2 import COLOR_BGR2GRAY, VideoCapture, destroyAllWindows, imshow, cvtColor, rectangle, resize, waitKey 
from pytesseract import image_to_boxes, image_to_string
import pytesseract
from fps import showfps
from time import time
from os import name

custom_config = r'--oem 3 --psm 6'
prev = time()
fps = 0.0
cap = VideoCapture('http://192.168.0.101:8080/video')
if name == 'posix':
    pass
else:
    p = r'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
    pytesseract.pytesseract.tesseract_cmd = p
while(True):
    ret, frame = cap.read()
    img = cvtColor(frame, COLOR_BGR2GRAY)
    prev, fps = showfps(frame, prev, fps)
    img = resize(img, (480,360))
    h, w = img.shape
    boxes = image_to_boxes(img, config=custom_config)
    for b in boxes.splitlines():
        b = b.split(' ')
        img = rectangle(img, (int(b[1]), h - int(b[2])), (int(b[3]), h - int(b[4])), (0, 255, 0), 2)
 
    imshow('frame',img)
    if waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
destroyAllWindows()