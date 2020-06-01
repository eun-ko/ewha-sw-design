import numpy as np
import cv2

img = cv2.imread("ori.jpg")
imgray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
w, h = imgray.shape[:2]
templ = cv2.imread("templ.jpg", cv2.IMREAD_GRAYSCALE)
templ_h, templ_w = templ.shape[:2]
res = cv2.matchTemplate(imgray, templ, cv2.TM_CCOEFF_NORMED)
loc = np.where(res >= 0.5)
for pt in zip(*loc[::-1]):
    cv2.rectangle(img, pt, (pt[0] + w, pt[1] + h), (0, 0, 255), 2)
cv2.imshow("res",img)
cv2.waitKey(0)

print(res)