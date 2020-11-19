import cv2
import numpy as np

img=cv2.imread("shapes.jpg",cv2.IMREAD_GRAYSCALE)
canny=cv2.Canny(img,150,250)
kernel=np.array([[-1,-1,-1],
                [-1,9,-1],
                [-1,-1,-1]])
canny=cv2.filter2D(canny,-1,kernel)
canny=cv2.dilate(canny,kernel)
_,threshold=cv2.threshold(canny,240,255,cv2.THRESH_BINARY)
contours,_=cv2.findContours(threshold,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
numberOfCircles,numberOfSqaures,numberOfRectangles,numberofTriangles=0,0,0,0
for cnt in contours:
    approx=cv2.approxPolyDP(cnt,0.032*cv2.arcLength(cnt,True),True)

    cv2.drawContours(canny,[approx],0,(255,255,255),1)

    x=approx.ravel()[0]
    y=approx.ravel()[1]-2
    if(cv2.contourArea(cnt,True)<-750):

        if len(approx)==3:
            cv2.putText(canny,"Triangle",(x,y),cv2.FONT_HERSHEY_COMPLEX,0.4,(255,255,255))
            numberofTriangles=numberofTriangles+1
        elif len(approx)==4:
            x1,y1,w,h=cv2.boundingRect(approx)
            aspectratio=float(w)/h
            if aspectratio>0.95 and aspectratio<1.05:
                cv2.putText(canny,"Sqaure",(x,y),cv2.FONT_HERSHEY_COMPLEX,0.4,(255,255,255))
                numberOfSqaures=numberOfSqaures+1
            elif aspectratio>1.1:
                cv2.putText(canny, "Rectangle", (x, y), cv2.FONT_HERSHEY_COMPLEX, 0.4, (255, 255, 255))
                numberOfRectangles=numberOfRectangles+1
        elif len(approx)>5:
            cv2.putText(canny, "circle", (x, y), cv2.FONT_HERSHEY_COMPLEX, 0.4, (255, 255, 255))
            numberOfCircles=numberOfCircles+1
cv2.imshow("shapes",canny)
print("number of squares:"+str(numberOfSqaures)+"\n","number of triangles:"+str(numberofTriangles)+"\n","number of circles:"+str(numberOfCircles)+"\n","number of rectangles:"+str(numberOfRectangles)+"\n")
cv2.waitKey(0)
cv2.destroyAllWindows()