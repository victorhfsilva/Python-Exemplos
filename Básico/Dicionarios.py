#Dicionários

dic1 = dict()
dic1["Nome"] = "Victor"
dic1["Idade"] = 28
dic1["E-mail"] = "victor@email.com"
print(dic1)

dic2 = {"Nome": "Amanda",
        "Idadde": "22",
        "E-mail": "amanda@email.com"}
print(dic2)

#Retorna verdadeiro se for um das chaves do dicionário
print("Nome" in dic1)
print("Victor" in dic1)

#Retorna uma lista das chaves e dos valores
print(dic1.keys())
print(dic1.values())
#Retorna uma lista de tuplas com os pares chave/valor
print(dic1.items())

#Itera pelas chaves e valores da lista
for i,j in dic1.items():
    print(i,j)

#Conta o número de ocorrências de cada valor na lista
lista = ["Victor","Amanda","Salazar", "Victor", "Amanda","Victor"]
contagem = dict()
for nome in lista:
    if nome not in contagem:
        contagem[nome] = 1
    else:
        contagem[nome] = contagem[nome]+1
print(contagem)

#Retorna o valor da chave se estiver presente no dicionário, caso não esteja retorna 0
print(contagem.get("Victor",0))
print(contagem.get("Geovana",0))