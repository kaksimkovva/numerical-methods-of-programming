import imp
import numpy as np
from scipy import optimize
from scipy.misc import derivative
import math

x0 = 0.87
y0 = 2.64
delta = 0.1
def f1(y):
  return 0.5 * math.cos(y - 1)

def f2(x):
  return 2 + math.cos(x)

df1_x0 = abs(derivative(f1,x0 + delta, n=1))
df2_x0 = abs(derivative(f2,x0 + delta, n=1))
df1_y0 = abs(derivative(f1,y0 + delta, n=1))
df2_y0 = abs(derivative(f2,y0 + delta, n=1))

if df1_x0 + df2_x0 < 1 and df1_y0 + df2_y0 < 1:
print ('1')

def iter (x,y,e):

xn = x
yn = y
xn1 = f2(x)
yn1 = f1(y)
n = 1

while ((abs(xn1-xn) >= e) & (abs(yn1-yn) >= e)):

xn = xn1
yn = yn1
xn1 = f2(yn)
yn1 = f1(xn)
n += 1

print ('simple iteration:')
print ('x=', xn, "\ny=", yn, "\nThe amount of iteration = ", n)
iter(x0, y0, 0.0001)

else:

print ('2')
def f3(x):
  return 3*x[0] * math.cos(x[1]) * 0.9, math.sin(x[0] * 0.6) - x[1] * 1.
