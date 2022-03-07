import pytesseract as pt
from cv2 import imread

p = r'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
img = 'diab_test.png'
# img = 'test.jpg'
img = imread(img)
custom_config = r'--oem 3 --psm 6'
pt.pytesseract.tesseract_cmd = p

text =pt.image_to_string(img, config= custom_config)
# text =pt.image_to_string(img)
print(text)

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
# cv2.waitKey(0)