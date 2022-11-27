import matplotlib.pyplot as plt
import numpy as np
import math

# Euler`s method

def f(x,y):
    return x + math.cos(y/math.sqrt(0.3))

x0 = 1.4
b = 2.4
h = 0.1
x = np.arange(x0, b+h, h)
n = len(x)-1
y = np.empty(n+1)
y[0]=2.2

for i in range(n):
    y[i+1]=y[i]+f(x[i], y[i]) * h
y_rounded = np.round(y,4)
print('x= ', x, '\n y = ', y_rounded)

plt.show(x, y, 'o', x, y, 'red')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Euler’s method ')
plt.legend(['points', 'x+cos(y/sqrt(0.3))'])
plt.grid()
plt.show()



# Euler–Cauchy method

def f(x,y):
    return x + math.sin(y/math.sqrt(0.3))

x0 = 0.6
b = 1.6
h = 0.1
x = np.arange(x0, b+h, h)
n = len(x)-1
y = np.empty(n+1)

for i in range(n):
    y[i+1]=y[i]+(f(x[i], y[i]) + f(x[i+1], y[i] + h * f(x[i], y[i]))) * h/2
y_rounded = np.round(y,4)
print('x= ', x, '\n y = ', y_rounded)

plt.plot(x, y, 'o', x, y, 'red')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Euler–Cauchy method')
plt.legend(['points', 'x+sin(y/sqrt(0.3))'])
plt.grid()
plt.show()
