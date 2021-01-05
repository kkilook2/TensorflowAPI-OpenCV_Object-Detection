import cv2

src = cv2.imread("black_bird_img.jpg")
dst = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)

cv2.imshow("dst", dst)
cv2.waitKey(0)
cv2.destroyAllWindows()