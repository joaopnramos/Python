# -*- coding: utf-8 -*-
"""
Created on Mon Nov 13 17:55:36 2017

@author: joaop
"""
larg=float(input("Largura da parede: "))
alt=float(input("Altura da parede: "))
Area_da_parede=larg*alt
print("A sua parede tem a dimensão de {}x{} e sua área é {} metros quadrados.".format(larg,alt,Area_da_parede))

tinta=Area_da_parede/2
print("Para pintar a parede vai precisar de {}l de tinta.".format(tinta))


#Novo
import random
nome_1 =input('(1° jogador) Digite o seu nome: ')#2
nome_2=input('(2° jogador) Digite o seu nome: ')#3
nome_3=input('(3° jogador) Digite o seu nome: ')#4

sort=random.randint(1,3)


if sort == 1:#6
    print( 'Parabéns',nome_1,'Você Ganhou!!')
elif sort == 2:#7
    print( 'Parabéns',nome_2,'Você Ganhou!!')
elif sort == 3: #8
    print( 'Parabéns',nome_3,'Você Ganhou!!')