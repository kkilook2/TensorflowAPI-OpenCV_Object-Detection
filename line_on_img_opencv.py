import cv2
import numpy as np

blue_color = (255,0,0)
green_color = (0,255,0)
red_color = (0,0,255)
white_color = (255,255,255)

img  = np.zeros((384,384,3), np.uint8) +255 ## + �� �� â ��� ���� ���Ѵ�. 255�� ��� + 0�� ������


img = cv2.line(img, (10,10), (350,350), blue_color,5,shift=0)

cv2.imshow('imgshow', img)

cv2.waitKey(0)
cv2.destroyAllWindows()