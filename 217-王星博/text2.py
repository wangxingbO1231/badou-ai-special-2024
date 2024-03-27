import cv2
from PIL import Image
import matplotlib.pyplot as plt
import numpy as np
from skimage.color import rgb2gray
MAX = 2
def function(img):                 #放大函数
    height,width,channels = img.shape
    emptyTmage = np.zeros((MAX,MAX,channels),np.uint8)
    sh = MAX/height
    sw = MAX/width
    for i in range(MAX):
        for j in range(MAX):
            x=int(i/sh+0.5)
            y=int(j/sw+0.5)
            emptyTmage[i,j]=img[i,j]
    return emptyTmage
img = cv2.imread("C:/Users/13616/Desktop/zhaopian.jpg")
zoom = function(img)
print(zoom)
print(zoom.shape)
cv2.imshow("nearest interp",zoom)
cv2.imshow("image",img)
cv2.waitKey(0)