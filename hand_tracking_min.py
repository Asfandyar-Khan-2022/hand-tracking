import cv2
import mediapipe as mp
import time 

# define a video capture object
vid = cv2.VideoCapture(0)

mpHands = mp.solutions.hands
hands = mpHands.Hands()
mpDraw = mp.solutions.drawing_utils

pTime = 0
cTime = 0

while(True):

    # grab video data and return boolean value for ret
    ret, frame = vid.read()

    # convert image to BGR2RGB colour space
    imgRGB = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # process the image
    results = hands.process(imgRGB)

    # print(results.multi_hand_landmarks)

    # if a hand is detected then do the following
    if results.multi_hand_landmarks:

        # handLms contains data for each hand displayed on the webcam
        for handLms in results.multi_hand_landmarks:

            # get the landmarks and the id number
            for id, lm in enumerate(handLms.landmark):

                # ratio of pixel value
                print(id,lm)

                # multiply the ratio to get the pixel value
                # hight, width, channel
                h, w, c = frame.shape

                # postion of center, the position of each point can be found
                cx, cy = int(lm.x*w), int(lm.y*h)
                print(id, cx, cy)

                # if the id value is zero (landmark 0) then draw a purple dot of size 20
                if int(id) == 0:
                    cv2.circle(frame, (cx, cy), 20, (255, 0, 255), cv2.FILLED)
                    






            # draw the points and draw a line through them
            # connect the lines using HAND_CONNECTIONS
            mpDraw.draw_landmarks(frame, handLms, mpHands.HAND_CONNECTIONS)
    
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

# close the cap(the webcam)
vid.release()

# destroy all windows
cv2.destroyAllWindows()