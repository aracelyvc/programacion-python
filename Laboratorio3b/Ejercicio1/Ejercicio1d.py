#Aracely Velázquez Calderón
#Laboratorio 3b
#Dic. 2016
#Ejercicio 1d

import matplotlib.pyplot as plt
import numpy as np
import math

t=np.linspace(0,24,100)
h=math.e**(-1*t)
plt.plot(t,h,linewidth=5,color='r',label='Funcion: h(t)')
plt.legend()
plt.title('Ejercicio 1. d)')
plt.xlabel('Horas')
plt.ylabel('Kilometros')
plt.grid(True)
plt.show()
