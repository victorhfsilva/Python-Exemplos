#Tuples: são imútaveis, não é possível alterar seus valores uma vez criada
#São mais eficientes que listas
tupla1 = (5, 4, 3, 2, 1)

#Tuplas também podem ser utilizadas no lado esquerdo de atribuições
(a,b,c,d,e) = tupla1
print(c)

#Tuplas podem ser utilizadas em comparações: compara a sequência de números
tupla_comparacao = (3,2,5,4,2) > (3,2,5,5,3)
print(tupla_comparacao)

dic = {"a":10,"c":4,"d":12,"b":9}
lista_tuplas_dic = dic.items()

#Ordena o dicionário pelas chaves
print(sorted(lista_tuplas_dic))

#Ordena o dicionário pelos valores
tmp = list()
for chave, valor in lista_tuplas_dic:
    tmp.append((valor,chave))
sorted_tmp = sorted(tmp)
i = 0
for chave, valor in sorted_tmp:
    tmp[i] = (valor, chave)
    i=i+1
print(tmp)

#Ordena o dicionário pelos valores
sorted_tmp = sorted([(valor ,chave) for chave,valor in lista_tuplas_dic])
tmp = [(chave, valor) for valor,chave in sorted_tmp]
print(tmp)