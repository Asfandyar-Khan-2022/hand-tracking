import cv2
import mediapipe as mp
import time 
import hand_tracking_module as htm

pTime = 0
cTime = 0
vid = cv2.VideoCapture(0)
detector = htm.handDetector()

while(True):

    # grab video data and return boolean value for ret
    ret, frame = vid.read()
    frame = detector.findHands(frame,)

    # change the hadnNo value to highlight different parts of the hand
    lmList = detector.findPosition(frame, point = 10)
    # findPosition(frame)
    if isinstance(lmList, list) != 0:
        print(lmList[4])

    # get the current time
    cTime = time.time()

    # the time different allows for the fps to be found
    fps = 1/(cTime-pTime)
    pTime = cTime

    # put the fps on the window and define how it will look 
    # and where on the window it will be placed
    cv2.putText(frame,str(int(fps)),(10, 70), cv2.FONT_HERSHEY_PLAIN,3,
                (255,0,255),3)

    # show the captured frame
    cv2.imshow('Image', frame)

    # break out of webcam if q is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break