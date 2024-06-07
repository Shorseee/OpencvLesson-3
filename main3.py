import cv2

img=cv2.imread("pika.png")
cv2.imshow("Original Image",img)

rotate_img=cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)
#cv2.ROTATE_180,cv2.ROTATE_90_COUNTERCLOCKWISE

cv2.imshow('Rotated Image', rotate_img)

cv2.waitKey(0)
cv2.destroyAllWindows()

