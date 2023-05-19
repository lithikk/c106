import cv2


face_classifier=cv2.CascadeClassifier("C:/Users/santh/Downloads/106-class-acitivity-main/106-class-acitivity-main/haarcascade_frontalface_default.xml")
vid=cv2.VideoCapture(0)
while(True):
    ret,frame=vid.read()
    grey=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    faces=face_classifier.detectMultiScale(grey,1.1,5)
    for x,y,w,h in faces:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
    cv2.imshow("img",frame)
    cv2.waitKey(0)

vid.release()
cv2.destroyAllWindows()