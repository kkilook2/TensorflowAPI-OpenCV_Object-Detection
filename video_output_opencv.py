import cv2

capture = cv2.VideoCapture("testvideo.avi")

while True:
    ret, frame = capture.read()
    if(capture.get(cv2.CAP_PROP_POS_FRAMES) == capture.get(cv2.CAP_PROP_FRAME_COUNT)):
        capture.open("testvideo.avi")
        
    
    cv2.imshow("videofrane", frame) 
    if cv2.waitKey(33) == ord('q'): 
        break

    print(capture.get(cv2.CAP_PROP_POS_MSEC)) ##동영상 출력 클래스 속성 출력!
    print(capture.get(cv2.CAP_PROP_FRAME_WIDTH)) ##동영상 출력 클래스 속성 출력!

capture.release()
cv2.destroyAllWindows()