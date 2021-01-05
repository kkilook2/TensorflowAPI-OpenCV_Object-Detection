import cv2

src = cv2.imread("moon_img.png")

dst = cv2.GaussianBlur(src,(5,5), 4,4,borderType=cv2.BORDER_ISOLATED)

cv2.imshow("dst", dst)
cv2.waitKey(0)
cv2.destroyAllWindows()