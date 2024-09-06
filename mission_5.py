# 밝기 어둡게, 가운데 반짝이는 부분들은 살리되 하늘 부분은 어둡게 해서 멋있게

import cv2, sys
import numpy as np

src = cv2.imread('mission/05.png')

if src is None:
    sys.exit('Image load failed')

# median filter로 노이즈 제거
dst = cv2.medianBlur(src, 3)
gb_dst = cv2.GaussianBlur(dst, (5, 5), 0)

# sharpening 과정을 통해 에지 강조
kernel = np.array([[-1,-1,-1], [-1,9,-1], [-1,-1,-1]], dtype = np.float32)
sharpened = cv2.filter2D(gb_dst, -1, kernel)

# 밝기 조정 (약간 어둡게)
darker = cv2.addWeighted(sharpened, 0.8, np.zeros(sharpened.shape, sharpened.dtype), 0, 0)

# 명암 조절 (낮추기)
alpha = 0.1
final = np.clip((1+alpha)*darker - 128*alpha, 0, 255).astype(np.uint8)


cv2.imshow('src', src)
cv2.imshow('dst', final)

cv2.waitKey()
cv2.destroyAllWindows()