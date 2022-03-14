import cv2 as cv
import pytesseract
# import numpy as np


p = r'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
custom_config = r'--oem 3 --psm 6'

cap = cv.VideoCapture('http://192.168.0.102:8080/video')
pytesseract.pytesseract.tesseract_cmd = p
while(True):
    ret, frame = cap.read()
    img = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    img = cv.resize(img, (480,360))
    h, w = img.shape
    boxes = pytesseract.image_to_boxes(img, config=custom_config)
    for b in boxes.splitlines():
        b = b.split(' ')
        img = cv.rectangle(img, (int(b[1]), h - int(b[2])), (int(b[3]), h - int(b[4])), (0, 255, 0), 2)
 
    cv.imshow('frame',img)
    if cv.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv.destroyAllWindows()