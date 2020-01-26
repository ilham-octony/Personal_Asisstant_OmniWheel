import numpy as np
import cv2
import motor as motor
import time

cam = cv2.VideoCapture(0)
ball_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
b = 0
while True:
    Cball = 0
    
    ret, img = cam.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    ball = ball_cascade.detectMultiScale(gray, 1.3, 5)
    for (x,y,w,h) in ball:
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
        full =w+h
        tengah =x+(w/2)
        print("posisi x :", str(tengah))
        print("full"+str(full))
        if tengah < 270:
            motor.turnLeft()
            time.sleep(1.0)
            b+=1
            
        elif tengah > 370:
            motor.turnRight()
        else:
            motor.stop()

        if full > 470:
            motor.backward()
        elif full < 430:
            motor.forward()
        else:
            motor.stop()
    
        
    cv2.putText(img, "people : "+str(b), (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 1.0, (255, 0, 0),2,cv2.LINE_AA)    
    cv2.imshow('frame',img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
motor.cleanup()
cam.release()
cv2.destroyAllWindows()
