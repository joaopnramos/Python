# -*- coding: utf-8 -*-
"""
Created on Mon Nov 13 18:53:58 2017

@author: joaop
"""

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
    
    
    
    