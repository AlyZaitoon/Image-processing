import cv2
import numpy

left=cv2.imread("uttower_left.jpg",cv2.IMREAD_ANYCOLOR)
right=cv2.imread("uttower_right.jpg",cv2.IMREAD_ANYCOLOR)
images=[]
images.append(left)
images.append(right)
stitcher=cv2.Stitcher.create()
ret,pano=stitcher.stitch(images)
if ret==cv2.STITCHER_OK:
    cv2.imshow("pano",pano)
    cv2.waitKey(0)