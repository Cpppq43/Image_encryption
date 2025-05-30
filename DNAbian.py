A = 0
T = 1
G = 2
C = 3

# DNA-Encoding RULE #1 A = 00, T=11, G=01, C=10
dna0 = {}
dna0[0] = A
dna0[1] = G
dna0[2] = C
dna0[3] = T

dna1 = {}
dna1[0] = A
dna1[1] = C
dna1[2] = G
dna1[3] = T

dna2 = {}
dna2[0] = G
dna2[1] = A
dna2[2] = T
dna2[3] = C

dna3 = {}
dna3[0] = C
dna3[1] = A
dna3[2] = T
dna3[3] = G

dna4 = {}
dna4[0] = G
dna4[1] = T
dna4[2] = A
dna4[3] = C

dna5 = {}
dna5[0] = C
dna5[1] = T
dna5[2] = A
dna5[3] = G

dna6 = {}
dna6[0] = T
dna6[1] = G
dna6[2] = C
dna6[3] = A

dna7 = {}
dna7[0] = T
dna7[1] = C
dna7[2] = G
dna7[3] = A

import numpy as np


def dna_encode(b, g, r, way):
    b = np.unpackbits(b, axis=1)
    g = np.unpackbits(g, axis=1)
    r = np.unpackbits(r, axis=1)
    dna_dict = {
        0: dna0, 1: dna1, 2: dna2, 3: dna3,
        4: dna4, 5: dna5, 6: dna6, 7: dna7
    }
    dna = dna_dict[way]

    # 矢量化二进制到DNA的转换函数
    binary_to_dna = np.vectorize(lambda x, y: dna[(x << 1) | y])

    # 应用矢量化函数到每个颜色通道
    b_enc = binary_to_dna(b[:, ::2], b[:, 1::2])
    g_enc = binary_to_dna(g[:, ::2], g[:, 1::2])
    r_enc = binary_to_dna(r[:, ::2], r[:, 1::2])

    return b_enc, g_enc, r_enc


# 定义 DNA 碱基到二进制的映射
# 八种方式
dna_to_bits0 = {
    A: 0,  # 00
    G: 1,  # 01
    C: 2,  # 10
    T: 3  # 11
}

dna_to_bits1 = {
    A: 0,  # 00
    C: 1,  # 01
    G: 2,  # 10
    T: 3  # 11
}

dna_to_bits2 = {
    G: 0,  # 00
    A: 1,  # 01
    T: 2,  # 10
    C: 3  # 11
}
dna_to_bits3 = {
    C: 0,  # 00
    A: 1,  # 01
    T: 2,  # 10
    G: 3  # 11
}

dna_to_bits4 = {
    G: 0,  # 00
    T: 1,  # 01
    A: 2,  # 10
    C: 3  # 11
}
dna_to_bits5 = {
    C: 0,  # 00
    T: 1,  # 01
    A: 2,  # 10
    G: 3  # 11
}

dna_to_bits6 = {
    T: 0,  # 00
    G: 1,  # 01
    C: 2,  # 10
    A: 3  # 11
}

dna_to_bits7 = {
    T: 0,  # 00
    C: 1,  # 01
    G: 2,  # 10
    A: 3  # 11
}
dbs = [dna_to_bits0, dna_to_bits1, dna_to_bits2, dna_to_bits3, dna_to_bits4, dna_to_bits5, dna_to_bits6,
       dna_to_bits7]


def DNA_yunsuan(arr1_t: np.array, arr2_t: np.array, num, way=None) -> np.array:
    base_to_int = {C: 0, G: 1, A: 2, T: 3}
    int_to_base = {v: k for k, v in base_to_int.items()}
    arr1_num = np.vectorize(base_to_int.get)(arr1_t)
    arr2_num = np.vectorize(base_to_int.get)(arr2_t)
    fv1 = arr1_num ^ arr2_num
    fv2 = np.vectorize(int_to_base.get)(fv1)
    dna_to_bits = dbs[way]
    res = [
        (np.vectorize(dna_to_bits.get)(encoded)
         .reshape(encoded.shape[0], -1, 4)
         .dot([64, 16, 4, 1]))
        for encoded in fv2
    ]
    return np.array(res)
