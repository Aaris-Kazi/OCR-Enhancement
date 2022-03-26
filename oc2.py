from os import name
from cv2 import COLOR_BGR2GRAY, VideoCapture, cvtColor, resize, rectangle, imshow, waitKey, destroyAllWindows
import numpy as np
from pytesseract import image_to_boxes


ax1,ax2,ay1,ay2 =[],[],[],[] 


# img = imread('diab_test.png')
custom_config = r'--oem 3 --psm 6'

if name == 'posix':
    pass
else:
    import pytesseract as pt
    p = r'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
    pt.pytesseract.tesseract_cmd = p

cap = VideoCapture('http://192.168.0.101:8080/video')
def filtering(x1,y1,x2,y2):
    x1 = np.array(x1)
    y1 = np.array(y1)
    x2 = np.array(x2)
    y2 = np.array(y2)
    try:
        # print(x1.min(),y2.min(),x2.max(),y1.max())
        ax1.append(x1.min())
        ay1.append(y2.min())
        ax2.append(x2.max())
        ay2.append(y1.max())
    except ValueError:
        pass

def create_boxes(boxes):  
    bx1,bx2,by1,by2 =[],[],[],[]   
    for b in boxes.splitlines():
        b = b.split(' ')
        bx1.append(int(b[1]))
        bx2.append(int(b[3]))
        by1.append(h - int(b[2]))
        by2.append( h - int(b[4]))
    
    x1,x2,y1,y2 =[],[],[],[] 
    for i in range(len(bx1)):
        try:
            x = by2[i]
            y = by2[i+1]
            # print(x,y)
            if x > y-6 and y+6 > x:
                # print('positive')
                x1.append(bx1[i])
                y1.append(by1[i])
                x2.append(bx2[i])
                y2.append(by2[i])
            else:
                x1.append(bx1[i])
                y1.append(by1[i])
                x2.append(bx2[i])
                y2.append(by2[i])
                filtering(x1,y1,x2,y2)
                
                # print('negative')
                x1, x2 =[],[]
                y1, y2 =[],[]
        except Exception as e:
            x1.append(bx1[i])
            y1.append(by1[i])
            x2.append(bx2[i])
            y2.append(by2[i])
            filtering(x1,y1,x2,y2)
        
# img = cvtColor(img, COLOR_BGR2GRAY)
while(True):
    ret, frame = cap.read()
    img = cvtColor(frame, COLOR_BGR2GRAY)
    img = resize(img, (480,360))
    h, w = img.shape
    boxes = image_to_boxes(img, config=custom_config)
    create_boxes(boxes)
    for i in range(len(ax1)):
        rectangle(img, (ax1[i],  ay1[i]), (ax2[i], ay2[i]), (0, 255, 0), 2)
    
    ax1,ax2,ay1,ay2 =[],[],[],[] 
        # img = rectangle(img, (int(b[1]), h - int(b[2])), (int(b[3]), h - int(b[4])), (0, 255, 0), 2)
 
    imshow('frame',img)
    if waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
destroyAllWindows()