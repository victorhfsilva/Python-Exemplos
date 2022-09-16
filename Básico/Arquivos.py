#Arquivos

def gerarStringDados():
    nome = input("Insira um nome: ")
    email = input("Insira um email: ")
    telefone = input("Insira um telefone: ")
    cpf = input("Insira um cpf: ")
    string = "\n"+nome+";"+email+";"+telefone+";"+cpf;
    return string

#Open: cria o handle utilizado para ler um arquivo ('r' = read, 'w' = write, 'a'=append)
def criarHandleArquivo(nome,modo):
    try:
        arquivo = open(arquivo_nome,modo)
    except:
        print("Arquivo Inválido.")
        quit()
    return arquivo

arquivo_nome = input("Insira o nome do arquivo: ")
arquivo = criarHandleArquivo(arquivo_nome,'r')

#Lê dados de um arquivo csv e armazena em um dicionário
dicionario_pessoas = {}
for linha in arquivo:
    
    lista_dados = linha.strip().split(";")
    nome = lista_dados[0]
    email = lista_dados[1]
    telefone = lista_dados[2]
    cpf = lista_dados[3]
    
    dicionario_dados = {
        "Nome": nome,
        "Email": email,
        "Telefone": telefone,
        "CPF": cpf
    }
    
    dicionario_pessoas[nome]=dicionario_dados
    
else:
    print(dicionario_pessoas["Victor"])

#Escreve dados no arqivo CSV
continuar = True;
while continuar:
    continuar_str = input("Deseja inserir um valor? [Y/N] ")
    if continuar_str == 'Y' or  continuar_str == 'y':
        arquivo = open(arquivo_nome,'a')
        dados = gerarStringDados()
        arquivo.write(dados)
    elif continuar_str == 'N' or  continuar_str == 'n':
        continuar = False
    else:
        print("Entrada Inválida")
        

