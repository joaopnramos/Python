# -*- coding: utf-8 -*-
"""
Created on Mon Jan 22 12:15:37 2018

@author: joaop
"""

m = int(input('number of rows, m = '))
n = int(input('number of columns, n = '))
matrix = []; columns = []
# initialize the number of rows
for i in range(0,m):
  matrix += [0]
# initialize the number of columns
for j in range (0,n):
  columns += [0]
# initialize the matrix
for i in range (0,m):
  matrix[i] = columns
for i in range (0,m):
  for j in range (0,n):
    print ('entry in row: ',i+1,' column: ',j+1)
    matrix[i][j] = int(input())
print (matrix)




disciplinas=int(input("Quantas disciplinas tem?"))
anos=int(input("Quantos anos"))

for i in range(0,disciplinas): #percorrer linhas
    b.append([])     #adicionas uma segunda dentro da primeira
    for j in range(0,anos): #percorrer os as colunas 1 e 2
        b[i].append(int(input("numeros que deseja inserir na tabela: "))) #atribuis valor as colunas criadas