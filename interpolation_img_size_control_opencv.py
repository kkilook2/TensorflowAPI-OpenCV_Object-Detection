import cv2

src = cv2.imread("opencv_logo.png")

dst = src[280:300, 120:150] ## 400:480 -> 이미지 x축 범위 , 300:405 -> 이미지 y축 범위
dst = cv2.resize(dst, dsize=(256,256), interpolation=cv2.INTER_NEAREST) ## 설정범위를 256, 256으로 이웃 보간법으로 확대

cv2.imshow("dst", dst)
cv2.waitKey(0)
cv2.destroyAllWindows()