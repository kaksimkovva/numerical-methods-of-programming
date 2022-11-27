import matplotlib.pyplot as plt
from scipy.interpolate import UnivariateSpline
import numpy as np

x = [0.6, 0.7, 1, 1.5, 1.9]
y = [2.64, 3.73, 1.42, 1.84, 0.65]

spl = UnivariateSpline(x, y)#Побудовасплайна
xs = np.linspace(0, 4.5, 1000)
plt.plot(x,y,'ro', xs, spl(xs), 'g')
plt.show(
