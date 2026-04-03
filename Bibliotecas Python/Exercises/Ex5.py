import cv2
import numpy as np
import random as rd
import time

cap = cv2.VideoCapture('../babydance.mp4')
ret, frame = cap.read()
tamanho = frame.shape

cv2.imshow('frame', frame)
while(cap.isOpened()):
    ret, frame = cap.read()
    time.sleep(0.1)
    
    frame = cv2.flip(frame, 1)
    if(cv2.waitKey(1) == ord('q') or ret == False):
        break
    
    cv2.putText(frame, "Dance Baby, Dance!!", (rd.randint(100, tamanho[1] - 300), rd.randint(100, tamanho[0] - 300)), cv2.FONT_HERSHEY_SIMPLEX, 1.5, (0, 0, 255), 2)
    cv2.imshow('frame', frame)
    
cap.release()
cv2.destroyAllWindows()
