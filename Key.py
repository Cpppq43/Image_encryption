#生成一个随机图像 512x512 三通道
import cv2
import numpy as np
import random
img = np.zeros((512,512,3),np.uint8)
for i in range(512):
    for j in range(512):
        img[i,j] = [random.randint(0,255),random.randint(0,255),random.randint(0,255)]
cv2.imwrite("C:/Users/15003/Desktop/data/key.png",img)
#输出三个通道的值
b,g,r = cv2.split(img)
print(b)
print(g)
print(r)