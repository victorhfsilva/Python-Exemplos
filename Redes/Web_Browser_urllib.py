#urllib

#Web Browser
import urllib.request, urllib.parse, urllib.error

#Abre a página como se fosse um arquivo
handle = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')

#Conta o número de ocorrências de cada palavra
contagem = dict()
for linha in handle:
    linha = linha.decode().strip()
    print(linha)
    palavras = linha.split()
    for palavra in palavras:
        contagem[palavra] = contagem.get(palavra,0)+1

#Ordena o Dicionária em palavras mais frequentes
sorted_tmp = sorted([(valor ,chave) for chave,valor in contagem.items()], reverse=True)
contagem = [(chave, valor) for valor,chave in sorted_tmp]
print(contagem)

#Determina qual a palavra mais frequente e número de vez que ela é usada
(palavra_mais_frequente,numero_palavra_mais_frequente) = contagem[0]
print(palavra_mais_frequente,numero_palavra_mais_frequente)