#Strings

#Seleciona Letra de Palavra
palavra = input("Insira uma palavra: ").replace(" ","")
palavra_len = len(palavra)
i_str = input("Insira um número (de 1 a "+str(palavra_len)+"): ")
try:
    i = int(i_str)-1
    letra = palavra[i]
    print("Letra: ",letra)
except:
    print("Valor inválido")

#Soletra de Palavra
print("Soletrando ", palavra)
for i in palavra:
    print(i,end=" ")
else:
    print()

#Conta número de letras a na palavra
num_a = 0
if 'a' in palavra.lower():
    for i in palavra.lower():
        if i == 'a':
            num_a = num_a + 1
print("Número de As: ",num_a)

#Divide String
i_str = input("Insira o índice inicial (de 1 a "+str(palavra_len)+"): ")
j_str = input("Insira o índice final (de 1 a "+str(palavra_len)+"): ")
secao = ""
try:
    i = int(i_str)-1
    j = int(j_str)-1
    if i>=j:
        raise Exception("Seção Inválida")
    secao = palavra[i:j]
    print("Seção: ",secao)
except:
    print("Valor inválido")
    
#Encontra o índice de uma seção
if secao != "":
    print("Índice Inicial: ",palavra.find(secao)+1)

