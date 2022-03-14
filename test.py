# import pytesseract as pt

p = r'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
custom_config = r'--oem 3 --psm 6'
# img = 'diab_test.png'
# pt.pytesseract.tesseract_cmd = p

# text =pt.image_to_string(img, config= custom_config)

# print(text)

# import cv2
# import pytesseract

# img = cv2.imread('diab_test.png')
# pytesseract.pytesseract.tesseract_cmd = p
# h, w, c = img.shape
# boxes = pytesseract.image_to_boxes(img, config=custom_config) 
# for b in boxes.splitlines():
#     b = b.split(' ')
#     img = cv2.rectangle(img, (int(b[1]), h - int(b[2])), (int(b[3]), h - int(b[4])), (0, 255, 0), 2)

# cv2.imshow('img', img)
# # cv2.imwrite('gen1.png', img)
# cv2.waitKey(0)

import cv2
import pytesseract
import pandas as pd

img = cv2.imread('diab_test.png')
df = pd.read_csv('enhance.csv')
pytesseract.pytesseract.tesseract_cmd = p
h, w, c = img.shape
boxes = pytesseract.image_to_boxes(img, config=custom_config) 
# for b in boxes.splitlines():
#     b = b.split(' ')
#     img = cv2.rectangle(img, (int(b[1]), h - int(b[2])), (int(b[3]), h - int(b[4])), (0, 255, 0), 2)

for i in range(len(df)):
    x1 = df.X1.iloc[i]
    x2 =df.X2.iloc[i]
    y1 = df.Y1.iloc[i]
    y2 = df.Y2.iloc[i]
    img = cv2.rectangle(img, (x1,  y1), (x2, y2), (0, 255, 0), 2)
cv2.imshow('img', img)
cv2.imwrite('gen2.png', img)
cv2.waitKey(0)