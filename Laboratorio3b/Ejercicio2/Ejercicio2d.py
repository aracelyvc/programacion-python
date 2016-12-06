# -*- coding: utf-8 -*-
#Aracely Velázquez Calderón
#Laboratorio 3b
#Dic. 2016
#Ejercicio 2d

import matplotlib.pyplot as plt
import numpy as np
import math

t=np.linspace(0,2*math.pi,110)
f=(1+2*np.sin(t))*np.cos(t)
g=(1+2*np.sin(t))+np.sin(t)
plt.plot(f,t,linewidth=5,color='r',label='f(t)')
plt.plot(g,t,linewidth=5,color='k',label='g(t)')
plt.legend()
plt.title('Ejercicio 2.d')
plt.xlabel('Tiempo')
plt.ylabel('Metros')
plt.grid(True)
plt.show()
