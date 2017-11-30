#NANDゲートをパーセプトロンで実装

def NAND(x1, x2):
    w1, w2, theta = 0.5, 0.5, 0.7
    tmp = x1*w1 + x2*w2
    if tmp >= theta:
        return 0
    if tmp < theta:
        return 1

print(NAND(0, 0)) #1を出力
print(NAND(1, 0)) #1を出力
print(NAND(0, 1)) #1を出力
print(NAND(1, 1)) #0を出力
