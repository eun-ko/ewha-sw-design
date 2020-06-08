import numpy as np
import cv2

#불러오기와 흑백처리 (temp==매칭이미지)
tempgray = cv2.imread("image.png")

#템플릿 불러오기
templitgray = cv2.imread("template.png")

w, h = templitgray.shape[::2] # 템플릿 이미지 크기 저장
output = cv2.matchTemplate(tempgray, templitgray, cv2.TM_CCOEFF_NORMED) # 두 개의 이미지 비교

minimumValue, maximumValue, minimumLocation, maximumLocation = cv2.minMaxLoc(output)
leftTopLocation = maximumLocation
rightBottomLocation = (leftTopLocation[0] +w, leftTopLocation[1] + h)

threshold = 0.8  #정확도 조절가능, 일정 확률 이상 이미지가 비슷하면 True

flag = False
if np.amax(output) > threshold:
    flag = True

print(str(flag))
print((np.amax(output)))