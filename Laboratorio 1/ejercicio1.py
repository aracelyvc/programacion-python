#Aracely Velazquez Calderon
#Introduccion a la Programacion en python
#Laboratorio 1

def calcular(x):
    sum=0
    for i in range(1,x+1):
        sum=sum+i
    return sum
x = input()
print calcular(x)
