from scipy import integrate
import math

# Trapetzia method

eps = 0.001

def f1(x):
  return 1/math.sqrt(0.5*x+1)

def trap(f1,a,b,n):
  h=(b-a)/n
  sum=0.5*(f1(a)+f1(b))
  
  for i in range(1,n):
    sum+=f1(a+i*h)

  return sum*h

v,err = integrate.quad(f1,3.2,4)#Перевірка

if abs (trap(f1, 3.2, 4, 2*10) -trap(f1, 3.2, 4, 10))/3. <= eps:
    print("Trapetzia method:",round (trap(f1,3.2,4,10), 5))
    
print("Check for the trapetzia method= ",round(v, 5))

# Rectangle method

eps = 0.001

def f1(x):

  return math.log10(x+2)/x

def left_rec(f1,a,b,n):
  h=(b-a)/n
  sum=0
  
  for i in range(0,n):
    sum+=f1(a+i*h)

  return sum*h

v,err = integrate.quad(f1,1.2,2)#Перевірка


if abs(left_rec(f1,1.2,2,2*10) - left_rec(f1,1.2,2,10))/3. <=eps:
    print("left rectangle:",round (left_rec(f1,1.2,2,10), 5))

def right_rec(f1,a,b,n):
    h=(b-a)/n
    sum=0

    for i in range(1,n+1):
      sum+=f1(a+i*h)
     return sum*h

print("right rectangle:",round (right_rec(f1,1.2,2,10), 5))

def aver_rec(f1,a,b,n):
    h=0.08
    sum=0

    for i in range(0,n):
      sum+=f1(a+i*h)
    return sum*h

print("average rectangle:",round (aver_rec(f1,1.2,2,10), 5))
print("Check for the rectangle method= ",round (v, 5))

# Simpsone method

eps = 0.001

def f1(x):
  return (x+1)*math.sin(x)

def simpson(a,b,n):
    h = (b - a) / n
    integr = f1(a) + f1(b)

    for i in range(1,n):
      k = a + i*h
      if i%2 == 0:
        integr += 2 * f1(k)

      else:
        integr += 4 * f1(k)

    integr *= h/3

    return integr

if abs(simpson(1.6,2.4,2*8) -simpson(1.6,2.4,8))/ 15. <= eps:
print("Simpsone method:",round (simpson(1.6,2.4,8), 5))

v,err = integrate.quad(f1,1.6,2.4)#Перевірка
print("Check for the simpsone method= ",round(v, 5))
