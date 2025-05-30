import cv2
import numpy as np

# 定义函数添加高斯噪声
def add_gaussian_noise(image_path, output_path, variance=1e-7):
    img = cv2.imread(image_path)
    
    if img is None:
        print("Error: Image not found.")
        return

    img = img.astype(np.float32)
    
    # 计算标准差
    sigma = np.sqrt(variance)
    print(sigma)
    
    # 生成高斯噪声
    noise = np.random.normal(0, sigma, img.shape)
    img = img + noise
    
    # 限制像素值范围
    img = np.clip(img, 0, 255)
    img = img.astype(np.uint8)
    
    # 保存带噪声的图像
    cv2.imwrite(output_path, img)

# 使用函数
add_gaussian_noise(r"C:\Users\15003\Desktop\data\dec.png", r"C:\Users\15003\Desktop\data\Gaosi\gaosi.png", variance=1e-7)