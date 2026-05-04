import cv2
import numpy as np

cap = cv2.VideoCapture('Files/video_car.mp4')

# fourcc = cv2.VideoWriter_fourcc(*'MJPG')
# output = cv2.VideoWriter('novo_video.mp4', fourcc, 20.0, (640,480))

while(cap.isOpened()):
    ret, frame = cap.read()
    if ret == True:
        # output.write(frame)
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        cv2.imshow('frame', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break   
    else:
        break

cap.release()
# output.release()
cv2.destroyAllWindows()