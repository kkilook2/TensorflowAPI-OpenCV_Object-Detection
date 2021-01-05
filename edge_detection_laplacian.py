import cv2
import numpy as np

src = cv2.imread("car_way_white_line_img.jpg")

dst = cv2.Laplacian(src, cv2.CV_8U, ksize=1)

##dst = cv2.resize(dst,(1020,700), cv2.INTER_CUBIC)
cv2.imshow("dst", dst)
cv2.waitKey(0)
cv2.destroyAllWindows()