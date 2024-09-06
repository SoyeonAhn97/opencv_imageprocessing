###################################
########### 수정 진행 중 ###########
###################################

import cv2, sys
import numpy as np

src = cv2.imread('mission/01.png')

if src is None:
    sys.exit('Image load failed')

# GaussianBlur를 사용해 노이즈 제거&부드럽게 만들기
g_dst = cv2.GaussianBlur(src, (0, 0), 1)

# MedianBlur를 사용해 노이즈 제거&에지/텍스트 유지
m_dst = cv2.medianBlur(g_dst, 3)

# bilateral filter로 노이즈 제거
b_dst = cv2.bilateralFilter(m_dst, -1, 10, 5)

# Sharpening을 사용해 에지 강조
kernel = np.array([[-1,-1,-1], [-1,9,-1], [-1,-1,-1]])
s_dst = cv2.filter2D(b_dst, -1, kernel)

# 밝기 어둡게
final = cv2.subtract(s_dst, (20, 20, 20, 0))


cv2.imshow('src', src)
cv2.imshow('dst', final)

cv2.waitKey()
cv2.destroyAllWindows()