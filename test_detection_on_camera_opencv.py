import cv2
import numpy as np

capture = cv2.VideoCapture(0)
width = int(capture.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(capture.get(cv2.CAP_PROP_FRAME_HEIGHT))

while True:
    ret, frame = capture.read()

    src = frame
    dst = src.copy()

    image = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)

    circles = cv2.HoughCircles(image, cv2.HOUGH_GRADIENT, 1, 100, param1= 100, param2=35, minRadius=80, maxRadius=120)

    for i in circles[0]:
        cv2.circle(dst, (i[0], i[1] ), i[2], (255,255,255), 5)


    cv2.imshow("detection_on_camera", dst)

    key = cv2.waitKey(33)
    if key == ord('q'): break


capture.release()
cv2.waitKey(0)
cv2.destroyAllWindows()