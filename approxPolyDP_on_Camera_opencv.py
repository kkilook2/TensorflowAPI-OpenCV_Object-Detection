import cv2
import numpy as np

capture = cv2.VideoCapture(0)
width = int(capture.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(capture.get(cv2.CAP_PROP_FRAME_HEIGHT))

while True:
    ret, frame = capture.read()

    src = frame
    dst = src.copy()

    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3,3))

    gray = cv2.cvtColor(src, cv2.COLOR_RGB2GRAY)
    ret, binary = cv2.threshold(gray, 230, 255, cv2.THRESH_BINARY)
    morp = cv2.morphologyEx(binary, cv2.MORPH_CLOSE, kernel, iterations=2)
    image = cv2.bitwise_not(morp)

    contours, hierarchy = cv2.findContours(image, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

    for i in contours:
        perimeter = cv2.arcLength(i, True)
        epsilon = perimeter*0.05
        approx = cv2.approxPolyDP(i, epsilon, True)
        cv2.drawContours(dst, [approx], 0, (0,0,255),3, maxLevel=0)
        print([approx])
        for j in approx:
            cv2.circle(dst, tuple(j[0]),3,(255,0,0),-1)
    cv2.imshow("Conours_detection_on_camera", dst)

    
    key = cv2.waitKey(33)
    if key == ord('q'): break


capture.release()
cv2.waitKey(0)
cv2.destroyAllWindows()