#Expressões Matemáticas
var1 = 4
var2 = 6
print("Expressões Matemáticas");
soma = var1 + var2
print("Soma: ",soma)
subtracao = var2 - var1
print("Subtração: ",subtracao)
multiplicacao = var1 * var2
print("Multiplicação: ",multiplicacao)
divisao = var2 / var1 #Divisão em Python sempre resulta em um float
print("Divisão: ",divisao)
potencia = var1 ** var2
print("Potência: ", potencia)
resto = var2 % var1
print("Resto: ",resto,"\n")

#Strings
str1 = "Hello "
str2 = "World"
print("Strings")
concatenacao = str1+str2
print(concatenacao,"\n")

#Tipos de Variáveis
print("Tipos de Variáveis")
print(type(soma))
print(type(divisao))
print(type(concatenacao),"\n")

#Cast das Variáveis
print("Cast de Variáveis")
print(type(float(soma)))
print(type(int(divisao)))
print(type(str(potencia)),"\n")