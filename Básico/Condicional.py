#Operadores lógicos
menor = 10 < 20
menor_igual = 10 <= 20
maior = 10 > 20
maior_igual = 10 >= 20
igual = 10 == 20
diferente = 10 != 20

#If-else-elif: Python utiliza a identação (tabs) para determinar o início e o fim de um bloco
x_str = input("Insira um valor númerico.")
try:  
    x = float(x_str)
    if x < 10:
        print ("Menor que 10\n")
    elif x < 20:
        print("Menor que 20\n")
    else:
        print("Maior que 20\n")
except:
    print("Valor não númerico.\n")

y_str = input("Insira um valor de um a dez.")
try:
    y = float(y_str)
    match y:
        case 1:
            print("Um")
        case 2:
            print("Dois")
        case 3:
            print("Três")
        case 4:
            print("Quatro")
        case 5:
            print("Cinco")
        case 6:
            print("Seis")
        case 7:
            print("Sete")
        case 8:
            print("Oito")
        case 9:
            print("Nove")
        case 10:
            print("Dez")
        case _:
            print("Você não consegue contar este número com as mãos.")
except:
    print("Valor não númerico")

