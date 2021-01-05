import cv2
import numpy as np


src = cv2.imread("flower_01.jpg", cv2.IMREAD_GRAYSCALE)

kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(5,5), anchor = (-1,-1))
dst1 = cv2.erode(src, kernel, iterations=3)
dst2 = cv2.morphologyEx(src, cv2.MORPH_DILATE,kernel, iterations=3)
dst3 = cv2.morphologyEx(src, cv2.MORPH_OPEN,kernel, iterations=3)
dst4 = cv2.morphologyEx(src, cv2.MORPH_CLOSE,kernel, iterations=3)
dst5 = cv2.morphologyEx(src, cv2.MORPH_GRADIENT,kernel, iterations=1)
dst6 = cv2.morphologyEx(src, cv2.MORPH_TOPHAT,kernel, iterations=1)
dst7 = cv2.morphologyEx(src, cv2.MORPH_BLACKHAT,kernel, iterations=1)
dst8 = cv2.morphologyEx(src, cv2.MORPH_HITMISS,kernel, iterations=1)


dst = np.concatenate((src, dst6, dst7, dst8), axis=1)
cv2.imshow("dst", dst)
cv2.waitKey(0)
cv2.destroyAllWindows()