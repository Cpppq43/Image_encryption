#读取图片
import cv2
import numpy as np
import random

#加入椒盐噪声 取系数为0.05(占所有像素点的比例)
def salt(img,n):
    for k in range(n):
        i = int(np.random.random() * img.shape[1])
        j = int(np.random.random() * img.shape[0])
        if img.ndim == 2:
            img[j,i] = 255
        elif img.ndim == 3:
            img[j,i,0]= 255
            img[j,i,1]= 255
            img[j,i,2]= 255
    return img

img = cv2.imread(r"C:\Users\15003\Desktop\data\dec.png")
#加入椒盐噪声 取系数为0.05(占所有像素点的比例)
img = salt(img, int(0.05*img.shape[0]*img.shape[1]))

cv2.imwrite(r"C:\Users\15003\Desktop\data\Jiaoyan\0.05.png",img)