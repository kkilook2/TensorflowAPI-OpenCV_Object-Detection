import cv2

src = cv2.imread("opencv_logo.png")

dst = src[280:300, 120:150] ## 400:480 -> �̹��� x�� ���� , 300:405 -> �̹��� y�� ����
dst = cv2.resize(dst, dsize=(256,256), interpolation=cv2.INTER_NEAREST) ## ���������� 256, 256���� �̿� ���������� Ȯ��

cv2.imshow("dst", dst)
cv2.waitKey(0)
cv2.destroyAllWindows()