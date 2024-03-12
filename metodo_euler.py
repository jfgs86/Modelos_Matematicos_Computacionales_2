import numpy as np
import math
import matplotlib.pyplot as plt


#dx = lambda t,x: 0.001*x
#f = lambda x: 10*math.exp(0.001*t)

#dx = lambda t,x: 0.01*x
#f = lambda x: 10*math.exp(0.01*t)

#dx = lambda t,x: 0.1*x
#f = lambda x: 10*math.exp(0.1*t)

#dx = lambda t,x: -0.1*x
#f = lambda x: 10*math.exp(-0.1*t)

dx = lambda t,x: -0.01*x
f = lambda x: 10*math.exp(-0.01*t)


xi = 0
xf = 1
h = 0.1
n = int((xf - xi)/h)
t=0
x=10

#print('t \t\t x')
#print('%f \t %f'% (t, x))

t_plot= []
x_euler= []
x_analitica= []
pasos = 0

print("Iter \t tiempo \t x_euler \t x_analitica \t error")
for i in range(1, n+1):
    t_plot.append(t)
    x_euler.append(x)
    x_analitica.append(f(t))
    x = x + h * dx(t,x)
    t = t + h
    pasos += 1
    #if abs(x_analitica[-1] - x_euler[-1]) > 0.00001:
        #break
   
    print('%i \t %f \t %f \t %f \t %f'% (pasos, t, x, f(t), abs(f(t) - x) ))

t_plot.append(t)
x_euler.append(x)
x_analitica.append(f(t))

"""
plt.plot(t_plot, x_euler, label='Método de Euler')
plt.plot(t_plot, x_analitica,label='Solución análitica')
plt.xlabel('t')
plt.ylabel('x')
plt.legend()
plt.grid(True)
plt.savefig('Met_euler_e.png')
plt.show()
"""

