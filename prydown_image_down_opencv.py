import cv2

src = cv2.imread("tomato_img.jpg")
dst = src.copy()

for i in range(3): ## 1/2씩 3번 줄어드니까 1/2 * 1/2 * 1/2 = 1/8 씩 가로, 세로가 줄어들어서 총 면적은 1/64만큼 줄어든것!
    dst = cv2.pyrDown(dst)

cv2.imshow("dst", dst)
cv2.waitKey(0)
cv2.destroyAllWindows()