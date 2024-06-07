import cv2
img=cv2.imread("pika.png")

# Setting parameter values
#t_lower = 50  # Lower Threshold
#t_upper = 250  # Upper Threshold

# Applying the Canny Edge filter
edge=cv2.Canny(img,50,250)

cv2.imshow('original', img)
cv2.imshow('edge', edge)

cv2.waitKey(0)
cv2.destroyAllWindows()