from os import name
from cv2 import COLOR_BGR2GRAY, VideoCapture, cvtColor, resize, rectangle, imshow, waitKey, destroyAllWindows
from numpy import array, insert, delete
import numpy as np
from pytesseract import image_to_boxes