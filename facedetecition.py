import cv2 
img=cv2.imread("boy.jpg")
grey=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
face_classifier=cv2.CascadeClassifier("C:/Users/santh/Downloads/106-class-acitivity-main/106-class-acitivity-main/haarcascade_frontalface_default.xml")
faces=face_classifier.detectMultiScale(grey,1.1,5)
for x,y,w,h in faces:
    cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
    crop=img[y:y+h,x:x+h]
    cv2.imwrite("face.jpg",crop)
cv2.imshow("img",img)
cv2.waitKey(0)