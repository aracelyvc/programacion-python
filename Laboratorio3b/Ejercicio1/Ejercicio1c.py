# -*- coding: utf-8 -*-
#Aracely Velázquez Calderón
#Laboratorio 3b
#Dic. 2016
#Ejercicio 1c

import matplotlib.pyplot as plt
import numpy as np
import math

t=np.linspace(-1,5,120)
f=t*math.e**(-2*t)
plt.plot(t,f,linewidth=5,color='g',label='f(t)=te^(-2t)')
plt.legend()
plt.title('Ejercicio 1. c)')
plt.xlabel('Horas')
plt.ylabel('Kilometros')
plt.grid(True)
plt.show()
