import numpy as np
import cv2


src = cv2.imread("car_number.jpg", cv2.IMREAD_GRAYSCALE)
dst1 = cv2.pyrUp(src)
dst = cv2.Canny(dst1, 100, 200, apertureSize=3, L2gradient= True)
cv2.imshow("dst", dst)
cv2.waitKey(0)
cv2.destroyAllWindows()
