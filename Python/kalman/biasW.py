# -*- coding: utf-8 -*-
"""
Created on Thu Oct 15 09:03:37 2020
@author: xing
"""

import csv
import numpy as np
import matplotlib.pyplot as mp

# M 阶多项式 
M = 2
biasDiff = []
num = 0

dT = []
testx = []

i = 0

# firstT=0
firstS=0

x1 = 0
x2 = 0
x3 = 0
x4 = 0

y=0
xy = 0
x2y = 0

with open('1232.csv', 'r') as f:
    reader = csv.reader(f)
    # print(type(reader))
    
    for row in reader:
        firstT = float(row[2])
        firstS = float(row[0])
        break
    
    for row in reader:
        # dT.append(float(row[2]) - firstT)
        dT.append(row[1])
        
        x1 = x1 + float(row[1])
        x2 = x2 + float(row[1])**2
        x3 = x3 + float(row[1])**3
        x4 = x4 + float(row[1])**4
        
        y = y + float(row[0]) - firstS
        xy = xy + (float(row[0]) - firstS) * float(row[1])
        x2y = x2y + (float(row[0]) - firstS) * float(row[1])**2
        # Tlast = float(row[2])
        # biasDiff.append(row[1])
        biasDiff.append(float(row[0]) - firstS)
        num += 1
        testx.append(num)


a = np.asarray(biasDiff, dtype =  float)

x = np.asarray(dT, dtype =  float)
# x = np.asarray(testx, dtype =  float)

# mp.plot(x, a, lw = 1.0)
mp.scatter(x, a, lw = 1.0)

X=x
for i in range(2,M+1):
    X = np.column_stack((X, pow(x,i)))

X = np.insert(X,0,[1],1)

# 投影矩阵 (A^t * A)^-1 * A^t
# _w = (A^t * A)^-1 * A^t * y
# 正则化
# W = np.linalg.inv((X.T.dot(X))+np.exp(-7) * np.eye(M+1)).dot(X.T).dot(a)
# 无正则化
W2 = np.linalg.inv((X.T.dot(X))).dot(X.T).dot(a)

W =  np.zeros((3,1))
A = np.array([[num,x1,x2],[x1,x2,x3],[x2,x3,x4]])
b = np.array([[y],[xy],[x2y]])

A2 = np.linalg.inv(A)

A1 = np.array([[-0.537,0.416,-0.067],[0.334,-0.242,0.038],[-0.047,0.033,-0.005]])
# W = np.linalg.inv(A).dot(b)

# A1 = np.array([[6.38518256e-04,4.10232932e-02,-4.44921017e-01],[-1.09256295e-05,-9.10896511e-03,2.78687576e-01],[ 1.78574378e-06,-1.61249135e-04,-3.96471413e-02]])

c = A.dot(A1)

# W = A1.dot(b)



# W[0] = -0.101493999362
# W[1] = -0.350430995226
# W[2] = 0.024311399087

# W[0] = -0.067
# W[1] = 0.038
# W[2] = -0.005

# x = np.arange(10,80,1)

y_estimate=X.dot(W2)
# y_estimate2=X.dot(W)


mp.plot(x,y_estimate,'r',lw=2.0)
# mp.plot(x,y_estimate2,'g',lw=2.0)

mp.show()
