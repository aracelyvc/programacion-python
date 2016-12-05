#Aracely Velázquez Calderón
#Laboratorio 3b
#Dic. 2016
#Ejercicio 1a

import matplotlib.pyplot as plt
import numpy as np

x=np.linspace(-6,2,100)
y=5-4*x-x**2
plt.plot(x,y,linewidth=3,color='g',label='Parabola')
plt.legend()
plt.title('Ejercicio 1. a)')
plt.xlabel('Tiempo')
plt.ylabel('Metros')
plt.grid(True)
plt.show()
