import cv2
from cvzone.HandTrackingModule import HandDetector
cap =cv2.VideoCapture(0)
detector=HandDetector(detectionCon=0.8,maxHands=2)
cap.set(3, 1280)
cap.set(4, 720)

while True :
    SUCCESS,img=cap.read()
    #with draw
    hands,img= detector.findHands(img)
    #without drawing
    
    if hands:
        #hand1
        hand1=hands[0]
        lmList1=      hand1["lmList"]#lsit of 21 landmarks point
        bbox =        hand1["bbox"] #bbox info x,y,w,h
        centerPoint1= hand1["center"] #center of the hand
        handType1=    hand1["type"] #hand type
        # print(len(lmList1),lmList1)
        # print(bbox)
        fingers1= detector.fingersUp(hand1)    
        if(len(hands)==2):     
            hand2=hands[1]
            lmList2=      hand2["lmList"]#lsit of 21 landmarks point
            bbox =        hand2["bbox"] #bbox info x,y,w,h
            centerPoint2= hand2["center"] #center of the hand
            handType2=    hand2["type"] #hand type
            # print(handType1,handType2)            
            fingers2= detector.fingersUp(hand2)
            # length, info, img = detector.findDistance(lmList1[8], lmList2[8], img)
            length, info, img = detector.findDistance(centerPoint1, centerPoint2, img)
    #hands= detector.findHands(img)
    cv2.imshow("Image",img)
    cv2.waitKey(1)