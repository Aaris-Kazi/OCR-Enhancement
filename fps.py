import cv2 as cv
import time
FPS_SMOOTHING = 0.9

def showfps(frame, prev, fps): 
    now = time.time()
    fps = (fps*FPS_SMOOTHING + (1/(now - prev))*(1.0 - FPS_SMOOTHING))
    # print("fps: {:.1f}".format(fps))
    font = cv.FONT_HERSHEY_DUPLEX
    cv.putText(frame, "fps: {:.1f}".format(fps), (0, 56), font, 0.5, (0, 255, 0), 10)
    return now, fps