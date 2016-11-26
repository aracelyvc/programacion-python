#Aracely Velazquez Calderon
#Laboratorio 2
#25/11/2016
#Ejercicio 1

x=input("ingresa CO:")
y=input("ingresa CA:")
import math
def hip(x,y):
    z=math.sqrt(x*x+y*y)
    return z
print "la hipotenusa del triangulo es:", hip(x,y)
