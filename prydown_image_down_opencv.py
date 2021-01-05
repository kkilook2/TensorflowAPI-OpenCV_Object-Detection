import cv2

src = cv2.imread("tomato_img.jpg")
dst = src.copy()

for i in range(3): ## 1/2�� 3�� �پ��ϱ� 1/2 * 1/2 * 1/2 = 1/8 �� ����, ���ΰ� �پ�� �� ������ 1/64��ŭ �پ���!
    dst = cv2.pyrDown(dst)

cv2.imshow("dst", dst)
cv2.waitKey(0)
cv2.destroyAllWindows()