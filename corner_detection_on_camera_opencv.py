import cv2
import numpy as np

capture = cv2.VideoCapture(1)
width = int(capture.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(capture.get(cv2.CAP_PROP_FRAME_HEIGHT))

while True:
    ret, frame = capture.read()

    src = frame
    dst = src.copy()

    gray = cv2.cvtColor(src, cv2.COLOR_RGB2GRAY)
    corners = cv2.goodFeaturesToTrack(gray, 100, 0.01, 5, blockSize=3, useHarrisDetector=True, k=0.03)

    for i in corners:
        cv2.circle(dst, tuple(i[0]), 2, (255,0,0), 3)

    criteria =  (cv2.TERM_CRITERIA_MAX_ITER + cv2.TERM_CRITERIA_EPS, 30, 0.001)
    cv2.cornerSubPix(gray, corners, (5,5), (-1,-1), criteria)

    for i in corners:
        cv2.circle(dst, tuple(i[0]), 2, (0,0,255), 3)

    cv2.imshow("Conours_detection_on_camera", dst)

    key = cv2.waitKey(33)
    if key == ord('q'): break


capture.release()
cv2.waitKey(0)
cv2.destroyAllWindows()