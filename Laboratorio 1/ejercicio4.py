#Aracely Velazquez Calderon
#Introduccion a la Programacion en python 3
#Laboratorio 1

print "tiempo de viaje en: dias, horas, minutos, y segundos"
def tiempo(dias,horas,minutos,segundos):
    sum=0
    segundos=(86400*dias)+(3600*horas)+(60*minutos)+(1*segundos)
    sum=sum+segundos
    return sum

print tiempo
