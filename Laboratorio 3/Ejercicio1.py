#Aracely Velazquez Calderon
#Laboratorio 3
#29/11/2016
#Ejercicio 1

import matplotlib.pyplot as m
import math
x=input("ingesa la latitud  de tu primer punto:")
y=input("ingresa la longitudde tu primer punto")
u=input("ingresa la latitud de tu segundo punto:")
v=input("ingresa la longitud de tu segundo punto:")
a=(x,y)
b=(u,v)
def dist(a,b):
    x,y=a
    x=x*math.pi/180
    y=y*math.pi/180
    u,v=b
    u=u*math.pi/180
    v=v*math.pi/180
    d=6371.1*math.acos(math.sin(x)*math.sin(u)+math.cos(x)*math.cos(u)*math.cos(y-v))
    return d
print "la distancia en km. es:", dist(a,b)
