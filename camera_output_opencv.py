import cv2 

capture = cv2.VideoCapture(0)
capture.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

while True:
    print(capture.isOpened()) ## 카메라로 부터 동영상을 읽어 오는지 확인
    ## 아직 카메라가 없어서 false 뜸
    ret, frame = capture.read()
    if ret == True:
        cv2.imshow("VideoFrame", frame)
        if cv2.waitKey(33)== ord('q'): break

    else:
        break

capture.release()
cv2.destroyAllWindows()