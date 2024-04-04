def bilinear_interpolation(x, y, img):
    # 获取图像尺寸
    height, width = img.shape

    # 计算四个最近的像素坐标
    x1, y1 = int(x), int(y)
    x2, y2 = min(x1 + 1, width - 1), min(y1 + 1, height - 1)

    # 计算四个最近的像素值
    Q11, Q21 = img[y1, x1], img[y1, x2]
    Q12, Q22 = img[y2, x1], img[y2, x2]

    # 计算插值
    fxy1 = (x2 - x) * Q11 + (x - x1) * Q21
    fxy2 = (x2 - x) * Q12 + (x - x1) * Q22

    interpolated_value = (y2 - y) * fxy1 + (y - y1) * fxy2

    return interpolated_value

# 示例用法
import numpy as np
from PIL import Image

# 读取图像
img = np.array(Image.open('image.jpg').convert('L'))

# 双线性插值
x, y = 10.5, 15.5
interpolated_value = bilinear_interpolation(x, y, img)
print("Interpolated Value at ({}, {}): {}".format(x, y, interpolated_value))
