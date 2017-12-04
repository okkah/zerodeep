#ORゲートをパーセプトロンで実装

def OR(x1, x2):
    w1, w2, theta = 0.5, 0.5, 0.2
    tmp = x1*w1 + x2*w2
    if tmp <= theta:
        return 0
    elif tmp > theta:
        return 1

print(OR(0, 0)) #0を出力
print(OR(1, 0)) #1を出力
print(OR(0, 1)) #1を出力
print(OR(1, 1)) #0を出力
