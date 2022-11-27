import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import lagrange #імпортуємо функцію lagrange з бібліотки

x=np.array([-1,0,1,2], dtype=float)
y=np.array([5,-11,-3,23], dtype=float)

def lagranz(x,y,t):

  z=0

  for j in range(len(y)):

    p1=1; p2=1

      for i in range(len(x)):

        if i==j:

          p1=p1*1; p2=p2*1

        else:

          p1=p1*(t-x[i])

          p2=p2*(x[j]-x[i])

      z=z+y[j]*p1/p2

  return z

xnew=np.linspace(np.min(x),np.max(x),100) #точки, за якими будуємо графік
ynew=[lagranz(x,y,i) for i in xnew]

plt.plot(x,y,'o',xnew,ynew) #будуємо графік функції Лагранжа
plt.title('Lagrange Polynomial_1')
plt.grid(True)
plt.show()
