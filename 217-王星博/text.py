import cv2
from PIL import Image
import matplotlib.pyplot as plt
import numpy as np
from skimage.color import rgb2gray

#灰度化
img = cv2.imread("C:/Users/13616/Desktop/zhaopian.jpg")     #获取图像
h,w=img.shape[:2]           #获取图像的宽、高
img_gray = np.zeros([h,w],img.dtype)      #创建一个同等大小的空图片
for i in range(h):
    for j in range(w):
        m=img[i,j]
        img_gray[i,j]=int(m[0]*0.11 + m[1]*0.59 + m[2]*0.3)             #灰度处理
#print(m)
#print(img_gray)
#print("inage show gray: %s"%img_gray)
cv2.imshow("image show gray",img_gray)            #展示处理后的图片
cv2.waitKey(0)                    #展示时间，直到键盘输入
cv2.destroyAllWindows()