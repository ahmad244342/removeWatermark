import cv2

img = cv2.imread("safrudin.png")
img = cv2.resize(img, (600, 350))
mask = cv2.imread("safrudinMask.png")
mask = cv2.cvtColor(mask, cv2.COLOR_BGR2GRAY)
mask = cv2.resize(mask, (600, 350))
output = cv2.inpaint(img, mask, 3, flags=cv2.INPAINT_NS)

cv2.imshow("original", img)
cv2.imshow("mask", mask)
cv2.imshow("output", output)

cv2.waitKey(0)
