import cv2
import numpy as np

def sobel_edge_detection(image):
    # 转换为灰度图像
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # 计算 Sobel 边缘
    sobelx = cv2.Sobel(gray, cv2.CV_64F, 1, 0, ksize=3)
    sobely = cv2.Sobel(gray, cv2.CV_64F, 0, 1, ksize=3)

    # 计算边缘强度和方向
    magnitude = np.sqrt(sobelx**2 + sobely**2)
    direction = np.arctan2(sobely, sobelx)

    # 将边缘强度归一化到 [0, 255]
    magnitude = np.uint8(magnitude * 255 / np.max(magnitude))

    return magnitude, direction

# 读取图像
image = cv2.imread('image.jpg')

# Sobel 边缘检测
magnitude, direction = sobel_edge_detection(image)

# 显示结果
cv2.imshow('Original Image', image)
cv2.imshow('Sobel Magnitude', magnitude)
cv2.imshow('Sobel Direction', direction)
cv2.waitKey(0)
cv2.destroyAllWindows()
