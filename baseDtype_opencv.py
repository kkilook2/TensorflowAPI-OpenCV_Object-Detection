import cv2

capture = cv2.VideoCapture("testvideo.avi")

while True:
    ret, frame = capture.read()
    if(capture.get(cv2.CAP_PROP_POS_FRAMES) == capture.get(cv2.CAP_PROP_FRAME_COUNT)):
        capture.open("testvideo.avi")
    cv2.imshow("videofrane", frame)
    print(capture.isOpened())
    if cv2.waitKey(33) == ord('q'): break


capture.release()
cv2.destroyAllWindows()