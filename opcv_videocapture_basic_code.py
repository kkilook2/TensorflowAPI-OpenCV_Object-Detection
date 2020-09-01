##BASIC CODE##
import cv2

# videocapture(0 : 내장 웹캠, 1,2,3.. : 외부연결웹캠)
capture = cv2.VideoCapture(0)

capture.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

while(True):
    # video capture에서 데이터 읽기, ret와 frame
    ret, frame = capture.read()
    
    #video를 정상적으로 읽어오면 ret = True / 못 읽어오면 ret = False
    if ret == True :
        #imshow: 읽어온 video frame을 출력
        cv2.imshow("Video FRame", frame)
        
        #만약 종료하굎으면 키보드 : q 를 입력
        if cv2.waitKey(33) == ord('q'): break 
    else :
        break

capture.release()
cv2.destroyAllWindows()
