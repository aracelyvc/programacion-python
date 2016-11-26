#Aracely Velazquez Calderon
#Laboratorio 2
#25/11/2016
#Ejercicio 3

x=input("ingresa solo las cooerdenadas en x, para los vertices del triangulo:")
y=input("ingresa solo las cooerdenadas en y, para los vertices del triangulo:")
triangulo=([x],[y])
import matplotlib.pyplot as plt
plt.plot(triangulo)
plt.plot(triangulo[[0],[0]])
plt.show()

def funcion(triangulo):
    a=(triangulo[0],triangulo[0])
    b=(tiangulo[1],triangulo[1])
    c=(triangulo[2],triangulo[2])
    nt=[a,b,c]
    i=a+c/2
    nnt=[i,b,c]
    plt.plot(i,b,c)
    plt.show()
    j=b+c/2
    nnnt=[i,j,c]
    plt.plot(i,j,c)
    plt.show()
    k=i+c/2
    nnnnt=[k,j,c]
    plt.plot(k,j,c)
    plt.show()
    l=j+c/2
    nnnnnt=[k,l,c]
    plt.plot(k,l,c)
    plt.show()
    m=k+c/2
    nnnnnnt=[m,l,c]
    plt.plot(m,l,c)
    plt.show()
    n=l+c/2
    nnnnnnnt=[m,n,c]
    plt.plot(m,n,c)
    plt.show()
