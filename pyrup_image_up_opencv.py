import cv2

src = cv2.imread("image.jpg")

dst = cv2.pyrUp(src) ##���� ���� 2�辿 Ŀ��..

cv2.imshow("dst", dst)
cv2.waitKey(0)
cv2.destroyAllWindows()