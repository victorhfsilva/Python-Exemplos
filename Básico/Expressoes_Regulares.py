#Expressões Regulares

import re

#Retorna linhas que começam com Sa
arquivo = open("arquivo.csv")
for linha in arquivo:
    if re.search("^Sa", linha):
        print(linha.strip().split(";"))


