def chaos(m, d, rounds):
    x = 0.1
    y = 0.1
    z = 0.1
    w = 0.1
    u = 0.1
    for i in range(rounds):
        # 保留四位小数并进行计算
        x = round((15 * x - y * z + u) % 384, 13)
        y = round((x * z - 25 * y) % 512, 4)
        z = round((x * y - 65 * z - w) % 512, 13)
        w = round((y * z - m * w) % 8, 4)
        u = round((-d * x - y - 0.5 * u) % 8, 13)
    return x, y, z, w, u
