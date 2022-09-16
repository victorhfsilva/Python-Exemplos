#CSV
import csv

#Leitura
arquivo_csv = open("arquivo.csv","r")
leitor_csv = csv.reader(arquivo_csv,delimiter=";")
dicionario_pessoas = {}
for linha in leitor_csv:
    nome = linha[0]
    email = linha[1]
    telefone = linha[2]
    cpf = linha[3]
    dicionario_dados = {
        "Nome": nome,
        "Email": email,
        "Telefone": telefone,
        "CPF": cpf
    }
    dicionario_pessoas[nome]=dicionario_dados
else:
    print(dicionario_pessoas["Victor"])
    
#Escrita
arquivo_csv = open("arquivo.csv","a")
escritor_csv = csv.writer(arquivo_csv,delimiter=";", quotechar='"', quoting=csv.QUOTE_MINIMAL)
escritor_csv.writerow(["Sara","sara@email.com","1234-5678","098.765.432-12"])

    
