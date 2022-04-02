import cv2

image = cv2.imread('face_image.png')
image = cv2.resize(image, dsize=(0, 0), fx=0.25, fy=0.25, interpolation=cv2.INTER_LINEAR)

window_name = 'Image'
font = cv2.FONT_HERSHEY_SIMPLEX

org = (50, 50)

fontScale = 1
color = (255, 0, 0)
thickness = 2

# Using cv2.putText() method
image = cv2.putText(image, 'OpenCV Text Overlay Example', org, font,
				fontScale, color, thickness, cv2.LINE_AA)

# Displaying the image
cv2.imshow(window_name, image)
cv2.waitKey(0)
cv2.destroyAllWindows()
