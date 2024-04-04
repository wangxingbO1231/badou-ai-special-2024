import numpy as np
import cv2

def histogram_equalization(img):
    # 计算图像的直方图
    hist, bins = np.histogram(img.flatten(), 256, [0,256])

    # 计算累积分布函数
    cdf = hist.cumsum()
    cdf_normalized = cdf * hist.max() / cdf.max()

    # 创建均衡化后的图像
    equalized_img = np.interp(img.flatten(), bins[:-1], cdf_normalized)

    return equalized_img.reshape(img.shape)

# 读取图像
img = cv2.imread('image.jpg', cv2.IMREAD_GRAYSCALE)

# 直方图均衡化
equalized_img = histogram_equalization(img)

# 显示原始图像和均衡化后的图像
cv2.imshow('Original Image', img)
cv2.imshow('Equalized Image', equalized_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
