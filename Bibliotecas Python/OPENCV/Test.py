import cv2
import numpy as np

img = np.zeros((512, 512, 3), np.uint8)

cv2.line(img, (150, 0), (150, 512), (255, 255, 255), 5)
cv2.line(img, (350, 0), (350, 512), (255, 255, 255), 5)

cv2.line(img, (0, 150), (512, 150), (255, 255, 255), 5)
cv2.line(img, (0, 350), (512, 350), (255, 255, 255), 5)

cv2.rectangle(img, (200, 200), (300, 300), (0, 255, 0), -1)
cv2.circle(img, (75, 75), 50, (0, 0, 255), -1)

# font = cv2.FONT_HERSHEY_SIMPLEX
# text = "Hello World"

# cv2.putText(img, text, (50, 500), font, 1.5, (191, 0, 191), 4, cv2.LINE_AA)

cv2.imshow('tic', img)
cv2.waitKey(0) & 0xFF
cv2.destroyAllWindows()