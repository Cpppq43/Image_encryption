import datetime

from Arnold import *
from DNAbian import *
from chaos import *

rounds = 200


def encryption():
    global rounds
    # 自定义参数
    m = 200
    d = 20
    # 生成混沌序列
    result = chaos(m, d, rounds)
    print("first result:", result)

    # 读取图片
    img = cv2.imread(r"C:\Users\25402\Desktop\cpqnmsl\data\test.png")

    # 设置参数 a,b,rounds为混沌序列的前三位
    arnold_a = int(result[0])
    arnold_b = int(result[1])
    arnold_times = int(result[2])
    encode1_way = int(result[3])
    decode_way = int(result[4])
    print(arnold_a, arnold_b, arnold_times, encode1_way, decode_way)

    # 明文图像进行Arnold置乱
    img_encoded = arnold_encode(img, arnold_a, arnold_b, arnold_times)

    # 明文图像进行进行DNA编码
    b, g, r = cv2.split(img_encoded)
    enc = dna_encode(b, g, r, encode1_way)
    print(enc)

    # ---------------------------------------------------------------------------------------------------------------------
    # 加载密钥图像
    print("加载密钥图像..")
    key = cv2.imread(r"C:\Users\25402\Desktop\cpqnmsl\data\key.png")
    # 自定义参数
    m = 200
    d = 20
    # 生成混沌序列
    result = chaos(m, d, rounds)
    print("second result:", result)
    # 读取图片
    # 设置参数 a,b,rounds为混沌序列的前三位
    arnold_a = int(result[0])
    arnold_b = int(result[1])
    arnold_times = int(result[2])
    encode1_way = int(result[3])
    decode_way = int(result[4])
    print(arnold_a, arnold_b, arnold_times, encode1_way, decode_way)
    # 对密钥图像进行Arnold置乱
    key_encoded = arnold_encode(key, arnold_a, arnold_b, arnold_times)

    # 对密钥图像进行DNA编码
    b, g, r = cv2.split(key_encoded)
    key_enc = dna_encode(b, g, r, encode1_way)
    print(key_enc)

    # ---------------------------------------------------------------------------------------------------------------------
    # 对明文图像进行加密  转换enc和key_enc为Numpy数组
    enc = np.array(enc)
    key_enc = np.array(key_enc)
    print(enc)
    print("----------------------------------")
    print(key_enc)

    # 对三个通道进行运算
    b_dec, g_dec, r_dec = DNA_yunsuan(enc, key_enc, 2, decode_way)

    # 合并三个通道 转换为图像保存
    dec = cv2.merge([b_dec, g_dec, r_dec])
    cv2.imwrite(r"C:\Users\25402\Desktop\cpqnmsl\data\dec.png", dec)


def decryption():
    global rounds

    # 使用第二轮参数
    print("加载密钥图像..")
    key = cv2.imread(r"C:\Users\25402\Desktop\cpqnmsl\data\key.png")
    # 自定义参数
    m = 200
    d = 20
    # 生成混沌序列
    result = chaos(m, d, rounds)
    print("second result:", result)
    # 设置参数 a,b,rounds为混沌序列的前三位
    arnold_a = int(result[0])
    arnold_b = int(result[1])
    arnold_times = int(result[2])
    encode1_way = int(result[3])
    decode_way = int(result[4])
    print(arnold_a, arnold_b, arnold_times, encode1_way, decode_way)
    # 对密钥图像进行Arnold置乱
    key_encoded = arnold_encode(key, arnold_a, arnold_b, arnold_times)

    # 对密钥图像进行DNA编码
    b, g, r = cv2.split(key_encoded)
    key_enc = dna_encode(b, g, r, encode1_way)
    print(key_enc)

    # 加载密文图像
    print("加载密文图像..")
    enc = cv2.imread(r"C:\Users\25402\Desktop\cpqnmsl\data\dec.png")
    # 对密文图像进行DNA编码
    b, g, r = cv2.split(enc)
    enc = dna_encode(b, g, r, decode_way)

    enc = np.array(enc)
    key_enc = np.array(key_enc)

    # DNA解密
    # 自定义参数
    m = 200
    d = 20
    # 生成混沌序列

    result = chaos(m, d, rounds)
    print("first result:", result)
    # 设置参数 a,b,rounds为混沌序列的前三位
    arnold_a = int(result[0])
    arnold_b = int(result[1])
    arnold_times = int(result[2])
    encode1_way = int(result[3])
    decode_way = int(result[4])
    print(arnold_a, arnold_b, arnold_times, encode1_way, decode_way)

    # 对三个通道进行运算
    b_dec, g_dec, r_dec = DNA_yunsuan(enc, key_enc, 2,encode1_way)

    # 合并三个通道 进行Arnold解密
    dec = cv2.merge([b_dec, g_dec, r_dec])
    dec = dearnold_encode(dec, arnold_a, arnold_b, arnold_times)
    cv2.imwrite(r"C:\Users\25402\Desktop\cpqnmsl\data\RE.png", dec)


if __name__ == '__main__':
    starttime = datetime.datetime.now()
    encryption()
    t2 = datetime.datetime.now()
    print("加密时间：", datetime.datetime.now() - starttime)
    decryption()
    print("解密时间：", datetime.datetime.now() - t2)
