import cv2
import mediapipe as mp
import time 

# define a video capture object
vid = cv2.VideoCapture(0)

mp_hands = mp.solutions.hands
hands = mp_hands.Hands()
mpDraw = mp.solutions.drawing_utils

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
            # draw the points and draw a line through them. using mpDraw function
            mpDraw.draw_landmarks(frame, handLms, mp_hands.HAND_CONNECTIONS)

    # show the captured frame
    cv2.imshow('Image', frame)

    # break out of webcam if q is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# close the cap(the webcam)
vid.release()
# destroy all windows
cv2.destroyAllWindows()