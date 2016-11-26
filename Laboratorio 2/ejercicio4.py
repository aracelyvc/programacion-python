#Aracely Velazquez Calderon
#Laboratorio 2
#25/11/2016
#Ejercicio 4

import matplotlib.pyplot as plt
n=input("ingrese el numero(4,5,6 o 8) de lados del poligono:")
def funcion(n):
    n=n
    if n==4:
        cuadrado=[[0,1,0,1],[1,0,0,1]]
        plt.plot(cuadrado)
        plt.plot(cuadrado[0],cuadrado[1])
        plt.show()
    elif n==5:
        pentagono=[[4,10,2.15,7,11.85],[1,1,6.71,10.23,6.71]]
        plt.plot(pentagono)
        plt.plot(pentagono[0],pentagono[1])
        plt.show()
    elif n==6:
        exagono=[[4,8,2,4,8,10],[1,1,4.46,7.93,7.93,4.46]]
        plt.plot(pentagono)
        plt.plot(exagono[0],[1])
        plt.show()
    elif n==8:
        octagono=[[4,7,1.88,1.88,4,7,9.12,9.12],[1,1,3.12,6.12,8.24,8.24,6.12,3.12]]
        plt.plot(octagono)
        plt.plot(octagono[0],octagono[1])
        plt.show()
