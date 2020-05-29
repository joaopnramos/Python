# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

#Exercicio 10

ds=input('Hoje qual é o dia da semana?')
print(ds)
type(ds)
numint=int(input('Que temperatura vai estar hoje?'))
print (numint)
type(numint)
numfloat=float(input('Qual é a od do Porto?'))
print(numfloat)
type(numfloat)
print('Hoje qual é o dia da semana:  {0} Que temperatura vai estar hoje: {1} Qual é a od do Porto:  {2}'.format(ds, numint, numfloat))

import math
dir(math)


#Booleanos True or False
#Exercicio 006

a=bool(eval(input('booleano a= ')))
b=bool(eval(input('booleano b= ')))
print (a or b)
print (a and b)
print (not a)
print (not b)
print (a or a)
print (b or b)





#Ex 009 Função triângulo

def area_tri (base, altura):
    atri=base*altura/2
    return atri 
a=int(input('Qual é a base?' ))
b=int(input('Qual é a altura?'))
print('Área do Triângulo=',area_tri(a,b))

    