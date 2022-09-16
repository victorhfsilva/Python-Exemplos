#Listas

lista1 = [1,2,3,5,6]
lista2 = [1,4,5]

print(max(lista1))
print(min(lista1)) 
print(len(lista1)) 
print(sum(lista1))
print(sum(lista1)/len(lista1)) #Média Aritmética

lista_vazia = list()

#Concatenando
lista3 = lista1 + lista2
print(lista3)

#Dividindo
secao = lista3[4:7]
print(secao)

#Remove e retorna o último termo
print(secao.pop())
print(secao)

#Anexa um valor
secao.append("String") #Listas admitem diferentes tipos
print(secao)

#Ordena uma lista
lista3.sort()
print(lista3)

#Retorna o valor em um índice específico
print(lista3.index(4))

#Conta o número de ocorrências de um valor
print(lista3.count(1))

#Imprime os métodos disponíveis em uma lista
#print(dir(lista3))