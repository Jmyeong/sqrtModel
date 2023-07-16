import numpy as np
import matplotlib.pyplot as plt

n = 2 # sqrt number
num = 10 # x_axis range

def sqrt_x(n, num): # sqrt num, x_axis range
    arr = []
    for i in range(num):
        arr.append((i-num)**n)
    for i in range(num+1):
        arr.append(i**n)
    return arr

def x_axis(n, num): # sqrt num, x_axis range
    length = []
    for i in range(num):
        length.append(-len(sqrt_x(n,num))//2 + (i+1))
    for i in range(num+1):
        length.append(i)
    return length

plt.plot(x_axis(n,num),sqrt_x(n,num))
plt.show()
