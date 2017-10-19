import numpy as np
import cv2
import time

no_cascade = cv2.CascadeClassifier('nodetector.xml')
out_cascade = cv2.CascadeClassifier('outdetector.xml')
six_cascade = cv2.CascadeClassifier('sixdetector.xml')
four_cascade = cv2.CascadeClassifier('fourdetector.xml')

#img = cv2.imread('sachin.jpg')
#gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

countno = 0
countsix = 0
countout = 0
countfour = 0
run = 0
wicket = 0

cap = cv2.VideoCapture(0)

while(True and wicket <= 10):
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Our operations on the frame come here
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    nos = no_cascade.detectMultiScale(gray, 1.5, 6)
    outs = out_cascade.detectMultiScale(gray, 1.5, 6)
    sixes = six_cascade.detectMultiScale(gray, 1.5, 6)
    fours = four_cascade.detectMultiScale(gray, 1.5, 6)
    
    for (x,y,w,h) in nos:
        img = cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = img[y:y+h, x:x+w]
        if roi_gray.any():
            countno = countno +1
        if(countno > 5):   
            print "No Ball"
            run = run +1
            print "Scorecard : ", run , " /",wicket
            countno = 0
            countsix = 0
            countout = 0
            countfour = 0
            time.sleep(3) 

    for (x,y,w,h) in outs:
        img = cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = img[y:y+h, x:x+w]
        if roi_gray.any():
            countout = countout +1
        if(countout > 3):   
            print "Out"
            wicket = wicket + 1
            print "Scorecard : ", run , " /",wicket
            countno = 0
            countsix = 0
            countout = 0
            countfour = 0
            time.sleep(3)

    for (x,y,w,h) in sixes:
        img = cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = img[y:y+h, x:x+w]
        if roi_gray.any():
            countsix = countsix +1
        if(countsix > 10):   
            print "Six"
            run = run + 6
            print "Scorecard : ", run , " /",wicket
            countno = 0
            countsix = 0
            countout = 0
            countfour = 0
            time.sleep(3)

    for (x,y,w,h) in fours:
        img = cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = img[y:y+h, x:x+w]
        if roi_gray.any():
            countfour = countfour +1
        if(countfour > 2):   
            print "Four"
            run = run + 4
            print "Scorecard : ", run , " /",wicket
            countno = 0
            countsix = 0
            countout = 0
            countfour = 0
            time.sleep(3)          
    
    cv2.imshow('img',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
