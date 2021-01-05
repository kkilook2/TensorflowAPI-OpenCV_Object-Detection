import cv2
import numpy as np

capture = cv2.VideoCapture("testvideo.avi")
width = int(capture.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(capture.get(cv2.CAP_PROP_FRAME_HEIGHT))
videoWriter = cv2.VideoWriter()
isWrite = False

while True:
    ret, frame = capture.read()

    if(capture.get(cv2.CAP_PROP_POS_FRAMES) == capture.get(cv2.CAP_PROP_FRAME_COUNT)):
        capture.open("testvideo.avi")
    
    cv2.imshow("video", frame)
    key = cv2.waitKey(33)

    if key == ord('1'):  ## Ű���尪 1�� �Է¹����� ��ȭ ����
        fourcc = cv2.VideoWriter_fourcc(*'XVID')
        videoWriter.open("test_studio_video2.avi", fourcc, 30, (width, height), True)
        isWrite  = True

    elif key == ord('2'): ## Ű���尪 2�� �Է¹����� ��ȭ ���� ��, ��ȭ �Ϸ�� True ��ȯ
        print(videoWriter.isOpened())
        videoWriter.release()
        isWrite = False
        
    
    elif key == ord('q'): break

    if isWrite == True:
        videoWriter.write(frame)

videoWriter.release()

capture.release()
cv2.destroyAllWindows()