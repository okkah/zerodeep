#3層ニューラルネットワークのフォワード方向の実装

import numpy as np

def init_network():     #ディクショナリ型の変数networkに重みとバイアスを格納
    network = {}
    network['W1'] = np.array([[0.1, 0.3, 0.5], [0.2, 0.4, 0.6]])
    network['b1'] = np.array([0.1, 0.2, 0.3])
    network['W2'] = np.array([[0.1, 0.4], [0.2, 0.5], [0.3, 0.6]])
    network['b2'] = np.array([0.1, 0.2])
    network['W3'] = np.array([[0.1, 0.3], [0.2, 0.4]])
    network['b3'] = np.array([0.1, 0.2])

    return network

def forward(network, x):    #入力信号が出力へと変換されるプロセス
    W1, W2, W3 = network['W1'], network['W2'], network['W3']
    b1, b2, b3 = network['b1'], network['b2'], network['b3']

    a1 = np.dot(x, W1) + b1
    z1 = sigmoid(a1)
    a2 = np.dot(z1, W2) +b2
    z2 = sigmoid(a2)
    a3 = np.dot(z2, W3) + b3
    y = identify_function(a3)

    return y

def sigmoid(x):     #活性化関数h()（シグモイド関数）
    return 1 / (1 + np.exp(-x))

def identify_function(x):       #活性化関数σ()（出力層） 
    return x

network = init_network()
x = np.array([1.0, 0.5])
y = forward(network, x)
print(y)    #[0.31682708 0.69627009]
