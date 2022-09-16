#For Loops

#Itera uma lista
lista = [4, 6, 7, 2, 4, 1, 2]
for i in lista:
    print(i, end=" ")
else:
    print()

#Obtem o maior número da lista
maior_ate_agora = float('-inf')
for i in lista:
    if i > maior_ate_agora:
        maior_ate_agora = i
maximo = maior_ate_agora
print(maximo)

#Soma os valores da lista
soma = 0
for i in lista:
    soma = soma + i
print(soma)

#Itera de 0 a 10 (não inclui 10)
for i in range(10):
    print(i, end=" ")
else:
    print()

#Itera de 2 a 8 (não inclui 8)
for i in range(2,8):
    print(i, end=" ")
else:
    print()

#Itera de 3 a 13 em passos de 3 dígitos (não inclui 13)
for i in range (3,13,3):
    print(i, end=" ")
else:
    print()
    
#Nested For
for i in [0,1]:
    for j in [0,1]:
        print(str(i)+str(j),end=" ")
else:
    print()