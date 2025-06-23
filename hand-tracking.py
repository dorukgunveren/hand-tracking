import cv2 as cv
import time
import mediapipe as mp

id_names = {

    0 : "WRIST",
    1 : "THUMB_CMC",
    2 : "THUMB_MCP",
    3 : "THUMB_IP",
    4 : "THUMB_TIP",
    5 : "INDEX_FINGER__MCP",
    6 : "INDEX_FINGER_PIP",
    7 : "INDEX_FINGER_DIP",
    8 : "INDEX_FINGERTIP",
    9 : "MIDDLE_FINGER_MCP",
    10 : "MIDDLE_FINGER_PIP",
    11 : "MIDDLE_FINGER_DIP",
    12 : "MIDDLE_FINGER_TIP",
    13 : "RING_FINGER_MCP",
    14 : "RING_FINGER_PIP",
    15 : "RING_FINGER_DIP",
    16 : "RING_FINGER_TIP",
    17 : "PINKY_MCP",
    18 : "PINKY_PIP",
    19 : "PINKY_DIP",
    20 : "PINKY_TIP",

}

cap = cv.VideoCapture(0)

mpHand = mp.solutions.hands
hands = mpHand.Hands()             

mpDraw = mp.solutions.drawing_utils

pTime = 0
cTime = 0

while True:
    succes, frame = cap.read()         

    if not succes:
        break
    
    else:
        frameRGB = cv.cvtColor(frame, cv.COLOR_BGR2RGB)

        results = hands.process(frameRGB)
        
        thumb_tips = []

        if results.multi_hand_landmarks:
            for handLms in results.multi_hand_landmarks:
                mpDraw.draw_landmarks(frame, handLms, mpHand.HAND_CONNECTIONS)
                
                for id, lm in enumerate(handLms.landmark): 

                    if id in id_names:
                        name = id_names[id]
                        print(name, "\n", lm)

                    h, w, c = frame.shape
                    cx, cy = int(lm.x * w), int(lm.y * h)

                    if id == 4:
                        thumb_tips.append((cx, cy))
                        cv.circle(frame, (cx, cy), 8, (255, 0, 0), cv.FILLED)
                    
                    if len(thumb_tips) == 2:
                        cv.line(frame, thumb_tips[0], thumb_tips[1], (0, 255, 0), 2)

        cTime = time.time()
        fps = 1 / (cTime - pTime)
        pTime = cTime

        frame = cv.flip(frame, 1)
        cv.putText(frame, "FPS: " + str(int(fps)), (50, 100), cv.FONT_HERSHEY_PLAIN, 2, (0, 255, 0), 2)
        cv.imshow("Hand Tracking", frame)

        quit = cv.waitKey(1)
        if quit != -1:
            break