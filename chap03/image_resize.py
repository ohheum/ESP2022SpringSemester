import cv2

filename = "img.jpg"

imgColor = cv2.imread(filename, cv2.IMREAD_COLOR)

imgColor2 = cv2.resize(imgColor, dsize=(640, 480), 		interpolation=cv2.INTER_AREA)
imgColor3 = cv2.resize(imgColor, dsize=(0, 0), fx=0.5, fy=0.5, interpolation=cv2.INTER_LINEAR)

cv2.imshow("Color1", imgColor)
cv2.imshow("Color2", imgColor2)
cv2.imshow("Color3", imgColor3)

cv2.waitKey(0)
cv2.destroyAllWindows()
