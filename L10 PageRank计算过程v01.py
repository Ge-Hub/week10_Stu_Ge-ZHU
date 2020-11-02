#-*- encoding:utf-8 -*-
# numpy.dot(a, b, out=None) 二维数组则相当于矩阵乘积。一维数组则是内积 http://docs.scipy.org/doc/numpy/reference/generated/numpy.dot.html

import numpy as np
a = np.array([[0,0,0,1/3,0,0],
             [1/4,0,0,0,1/2,0],
             [0,1,0,1/3,1/2,0],
             [1/4,0,0,0,0,1],
             [1/4,0,1,1/3,0,0],
             [1/4,0,0,0,0,0]])

b = np.array([1/6, 1/6, 1/6, 1/6, 1/6, 1/6])
w = b

def work(a, w):
    for i in range(100):
        w = np.dot(a, w) 
        print(w)

def random_work(a, w, n):
    d = 0.85
    for i in range(100):
        w = (1-d)/n + d*np.dot(a, w)
        print(w)
        
# 简化模型 E=C>B>D>A>F
work(a, w)
#第100次迭代结果
#[1.47911420e-31 2.00000000e-01 4.00000000e-01 2.21867130e-31 4.00000000e-01 7.39557098e-32]

# 随机浏览模型 E>C>B>D>A>F

random_work(a, w, 4)
#第100次迭代结果
#[0.06432063 0.2685199  0.50991431 0.09466105 0.51141593 0.05116813]
