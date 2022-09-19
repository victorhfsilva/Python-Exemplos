import json

dados = '''{
    "nome" : "Victor",
    "telefone" : {
        "tipo" : "int1",
        "numero" : "1234-5678"
        },
    "email" : {
        "esconder" : "sim"
        }
    }'''

#Lê JSON de uma string
info = json.loads(dados)
print("Nome: ",info["nome"])
print("Esconder: ",info["email"]["esconder"])

#Lê JSON de um arquivo
arquivo = open("Victor.json",'r')
info = json.load(arquivo)
print("Nome: ",info["nome"])