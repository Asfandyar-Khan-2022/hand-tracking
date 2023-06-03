import cv2
import mediapipe as mp
import time 

# define a video capture object

class handDetector():
    def __init__(self, mode= False, maxHands = 2, complexity = 1, detectionCon = 0.5, trackCon=0.5):
        self.mode= mode
        self.maxHands = maxHands
        self.complexity = complexity
        self.detectionCon = detectionCon
        self.trackCon = trackCon

        self.mpHands = mp.solutions.hands
        self.hands = self.mpHands.Hands(self.mode, self.maxHands,
                                        self.complexity, self.detectionCon, self.trackCon)
        self.mpDraw = mp.solutions.drawing_utils
    
    def findHands(self, frame, draw=True):
        # convert image to BGR2RGB colour space
        imgRGB = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # process the image
        results = self.hands.process(imgRGB)

        # print(results.multi_hand_landmarks)

        # if a hand is detected then do the following
        if results.multi_hand_landmarks:

            # handLms contains data for each hand displayed on the webcam
            for handLms in results.multi_hand_landmarks:
                if draw:

                    # draw the points and draw a line through them
                    # connect the lines using HAND_CONNECTIONS
                    self.mpDraw.draw_landmarks(frame, handLms,
                                               self.mpHands.HAND_CONNECTIONS)
        return frame
            
                ## get the landmarks and the id number
                # for id, lm in enumerate(handLms.landmark):

                #     # ratio of pixel value
                #     print(id,lm)

                #     # multiply the ratio to get the pixel value
                #     # hight, width, channel
                #     h, w, c = frame.shape

                #     # postion of center, the position of each point can be found
                #     cx, cy = int(lm.x*w), int(lm.y*h)
                #     print(id, cx, cy)

                #     # if the id value is zero (landmark 0) then draw a purple dot of size 20
                #     if int(id) == 0:
                #         cv2.circle(frame, (cx, cy), 20, (255, 0, 255), cv2.FILLED)
                        



def main():
    pTime = 0
    cTime = 0
    vid = cv2.VideoCapture(0)
    detector = handDetector()

    while(True):

        # grab video data and return boolean value for ret
        ret, frame = vid.read()
        frame = detector.findHands(frame)

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
        print('TESTING')
        cv2.imshow('Image', frame)

        # break out of webcam if q is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

# # close the cap(the webcam)
# vid.release()

# # destroy all windows
# cv2.destroyAllWindows()

if __name__ == '__main__':
    main()