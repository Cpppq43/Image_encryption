import cv2
import numpy as np
import matplotlib.pyplot as plt

def dft2D(f):
    """
    通过计算一维傅里叶变换实现图像二维快速傅里叶变换
    Parameters:
        f: image (Gray scale)
    Return:
        the result of FFT
    """
    F = f.copy()
    F = F.astype(np.complex128)

    # FFT for each row
    for i in range(F.shape[0]):
        F[i] = np.fft.fft(F[i])
    
    # FFT for each column
    for i in range(F.shape[1]):
        F[:, i] = np.fft.fft(F[:, i])
    
    return F

def idft2D(F):
    """
    实现二维傅里叶逆变换
    Parameters:
        F : 灰度图像的傅里叶变换结果
    Return:
        傅里叶逆变换结果
    """
    # Conjugate
    f = F.conjugate()
    
    # 2D FFT
    for i in range(f.shape[0]):
        f[i] = np.fft.fft(f[i])
    for i in range(f.shape[1]):
        f[:, i] = np.fft.fft(f[:, i])
    
    # Divide by MN & Conjugate
    f = f/f.size
    f = np.abs(f.conjugate())

    return f

def main(filepath):
    """
    Main function for problem 3.
    """
    # Read the image
    img = cv2.imread(filepath, 0)
    img = img/255.

    # 2D FFT
    img_fft = dft2D(img)
    #存储傅里叶变换结果
    img_fft = np.fft.fftshift(img_fft)


    # 2D IFFT 
    img_ifft = idft2D(img_fft)

    # Cal difference
    img_diff = img - img_ifft

    # Plot the result)


if __name__ == "__main__":
    main(r"C:\Users\15003\Desktop\data\enc.png")
