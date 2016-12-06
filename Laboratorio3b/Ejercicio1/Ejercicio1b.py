# -*- coding: utf-8 -*-
#Aracely Velázquez Calderón
#Laboratorio 3b
#Dic. 2016
#Ejercicio 1b

import matplotlib.pyplot as plt
import numpy as np

x=np.linspace(-1,5,80)
y=2*x**2-8*x-11
plt.plot(x,y,linewidth=5,color='k',label='Parabola')
plt.legend()
plt.title('Ejercicio 1. b)')
plt.xlabel('Tiempo')
plt.ylabel('Metros')
plt.grid(True)
plt.show()
