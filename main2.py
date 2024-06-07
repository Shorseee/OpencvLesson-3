import cv2

img=cv2.imread("pika.png")
cv2.imshow("Original Image",img)

hsv_image= cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
cv2.imshow('HSV Image', hsv_image)

cv2.waitKey(0)
cv2.destroyAllWindows()