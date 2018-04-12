#Relu関数をグラフで表す

import numpy as np
import matplotlib.pylab as plt

def relu_function(x):
    return np.maximum(0, x)

x = np.arange(-5.0, 5.0, 0.1)
y = relu_function(x)
plt.plot(x, y)
plt.ylim(-1, 6)     #yの範囲を指定
plt.show()
