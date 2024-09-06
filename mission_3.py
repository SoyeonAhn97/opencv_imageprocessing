# 배경이 우글우글한 부분을 블러처리한 것 처럼 매끄럽게

import cv2, sys
import numpy as np

src = cv2.imread('mission/03.png')

if src is None:
    sys.exit('Image load failed')

# 노이즈 제거 & 부드럽게 만들기
g_dst = cv2.GaussianBlur(src, (5, 5), 1)
m_dst = cv2.medianBlur(g_dst, 3)

# sharpening 과정을 통해 에지 강조
kernel = np.array([[-1,-1,-1], [-1,9,-1], [-1,-1,-1]], dtype = np.float32)
sharpened = cv2.filter2D(m_dst, -1, kernel)

# 밝기 조정 (약간 어둡게)
final = cv2.addWeighted(sharpened, 0.8, np.zeros(sharpened.shape, sharpened.dtype), 0, 0)


# 처음 이미지 출력
cv2.imshow('src', src)
# 결과 이미지 출력
cv2.imshow('Processed Image', final)

cv2.waitKey(0)
cv2.destroyAllWindows()