from os import name
from cv2 import COLOR_BGR2GRAY, VideoCapture, cvtColor, resize, rectangle, imshow, waitKey, destroyAllWindows
from numpy import array, insert, delete
import numpy as np
from pytesseract import image_to_boxes


custom_config = r'--oem 3 --psm 6'
cap = VideoCapture(0)
count = 0
ax1,ax2,ay1,ay2 = array([]),array([]),array([]),array([])

def filtering(x1,y1,x2,y2,ax1,ax2,ay1,ay2,count):
    try:
        # print(x1.min(),y2.min(),x2.max(),y1.max())
        # global ax1, ax2, ay1, ay2, count
        ax1 = insert(ax1, len(ax1), x1.min())
        ay1 = insert(ay1, len(ax2), y2.min())
        ax2 = insert(ax2, len(ax2), x2.max())
        ay2 = insert(ay2, len(ay2),  y1.max())
        count+=1
    except ValueError:
        pass


# filtering(count)
def deletion(x1,y1,x2,y2):
    for i in range(len(x1)):
        x1 = delete(x1, i)
        y1 = delete(y1, i)
        x2 = delete(x2, i)
        y2 = delete(y2, i)
    return x1,y1,x2,y2

def create_boxes(boxes,ax1,ax2,ay1,ay2,count):  
    bx1,bx2,by1,by2 =array([]),array([]),array([]),array([]) 
    i = 0
    for b in boxes.splitlines():
        b = b.split(' ')
        bx1 = insert(bx1, len(bx1), int(b[1]))
        by1 = insert(by1, len(by1), int(b[2]))
        bx2 = insert(bx2, len(bx2), int(b[3]))
        by2 = insert(by2, len(by2), int(b[4]))
        # bx1.append(int(b[1]))
        # bx2.append(int(b[3]))
        # by1.append(h - int(b[2]))
        # by2.append( h - int(b[4]))
        i+=1
    
    x1,x2,y1,y2 =array([]),array([]),array([]),array([]) 
    j = 0
    for i in range(len(bx1)):
        try:
            x = by2[i]
            y = by2[i+1]
            # print(x,y)
            
            if x > y-6 and y+6 > x:
                # print('positive')
                x1 = insert(x1, len(x1), bx1[i])
                x2 = insert(x2, len(x2), bx2[i])
                y1 = insert(y1, len(y1), by1[i])
                y2 = insert(y2, len(y2), by2[i])
                # x1.append(bx1[i])
                # y1.append(by1[i])
                # x2.append(bx2[i])
                # y2.append(by2[i])
            else:
                x1 = insert(x1, len(x1), bx1[i])
                x2 = insert(x2, len(x2), bx2[i])
                y1 = insert(y1, len(y1), by1[i])
                y2 = insert(y2, len(y2), by2[i])
                filtering(x1,y1,x2,y2,ax1,ax2,ay1,ay2,count)
                
                # print('negative')
                x1,y1,x2,y2 = deletion(x1,y1,x2,y2)
                
        except Exception as e:
            x1 = insert(x1, len(x1), bx1[i])
            x2 = insert(x2, len(x2), bx2[i])
            y1 = insert(y1, len(y1), by1[i])
            y2 = insert(y2, len(y2), by2[i])
            filtering(x1,y1,x2,y2,ax1,ax2,ay1,ay2,count)
        j+=1



if name == 'posix':
    pass
else:
    import pytesseract as pt
    p = r'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
    pt.pytesseract.tesseract_cmd = p
    
while(True):
    ret, frame = cap.read()
    img = cvtColor(frame, COLOR_BGR2GRAY)
    img = resize(img, (480,360))
    h, w = img.shape
    boxes = image_to_boxes(img, config=custom_config)
    create_boxes(boxes,ax1,ax2,ay1,ay2,count)
    for i in range(len(ax1)):
        rectangle(img, (ax1[i],  ay1[i]), (ax2[i], ay2[i]), (0, 255, 0), 2)
    ax1,ay1,ax2,ay2 = deletion(ax1,ay1,ax2,ay2)
    imshow('frame', img)
    if waitKey(1) & 0xFF == ord('q'):
        break
    
cap.release()
destroyAllWindows()