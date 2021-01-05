import cv2

src = cv2.imread("image.jpg")

dst = cv2.pyrUp(src) ##가로 세로 2배씩 커짐..

cv2.imshow("dst", dst)
cv2.waitKey(0)
cv2.destroyAllWindows()