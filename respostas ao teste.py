#Grupo 1

def primosate(num)
    for i in range(2,num+1):
        if eprimo(i):
            print(i)
primosate(5)


def areaR (l1, l2):
    return l1*l2

lado1=int(input("Diga um dos lados do retangulo do qual deseja calcular a area:" ))
lado2=int(input("Diga o outro lado do retangulo do qual deseja calcular a area:"))
print("A area do rectangulo é: "+ str(areaR(lado1, lado2)))

area_do_retangulo.__doc__ 
#area_do_retangulo()

a=str(input("Pretende calcular mais alguma área, se sim, digite S , se nao digite N."))
while a=="S":
    area_do_retangulo()
else:
    print("Obrigado e volte sempre.")
    
    
    
    
    
s
Fazer a tabuada de qualquer numero

ou seja

Fazer uma função para calcular a tabuada e escreve-la no ecran, o programa deve
ler um numero introduzido pelo utilizador

numero=int(input("Digite o numero da tabuada que pretende calcular: "))
j=[]
for j in range(1,11):
    tabuada=numero*j
    print(str(numero)+ "x" + str(j) + "=" + str(tabuada) )





Criar uma array 4x2 e multiplar o numero da primeira coluna pela segunda e no fim devolver a soma
ex:
    
    |1|1|  -1
    |2|2|  -4
    |3|4|-12
    |5|10|-50


b=[] #criar uma array

for i in range(0,4): #percorrer linhas
    b.append([])     #adicionas uma segunda dentro da primeira
    for j in range(0,2): #percorrer os as colunas 1 e 2
        b[i].append(int(input("numeros que deseja inserir na tabela: "))) #atribuis valor as colunas criadas
    
c=[]

for d in range(0,4):
    c.append(b[d][0] * b[d][1])
    
total=0
for g in range(len(c)):
    total=total+c[g]        
print(total)
    
     
    
    
#Grupo2, 1) Este pseudocodigo serve para calcular o valor do numero de artigos.
#Grupo 2
v=0   
total = 0.0
n_artigos=int(input("Digite o nº de artigos: "))
custo=float(input("Digite o custo: "))
for j in range(0,n_artigos):
    v = float(input("Introduza o preço:"))
    total = total + v
print("O preço total dos artigos é: " + str(total))
    

range.__doc__
nao estou mesmo ahaa
range.__doc__
import math
math.sqrt.__doc__
while.__doc__
def.__doc__

n_artigos=int(input("Digite o nº de artigos: "))
custo=float(input("Digite o custo: "))
for j in range(0,n_artigos):
    print(j)