import cv2
import numpy as np

dog = cv2.imread("Files/dog.jpg", cv2.IMREAD_COLOR)
dog_cinza = cv2.imread('Files/dog.jpg', cv2.IMREAD_GRAYSCALE)
dog_transparente = cv2.imread('Files/dog.jpg', cv2.IMREAD_UNCHANGED)

cv2.imshow('dog', dog_cinza)
x = cv2.waitKey(0)
cv2.destroyAllWindows()