import math

#Entrada de Dados
print("Calcule a exponencial de um número.\n")
entrada = input("Insira um valor numérico.")
try: 
    entrada_float = float(entrada);
    exponencial = math.exp(entrada_float);
    print("A exponencial de ",entrada," é: ",exponencial);
except:
    print("Valor não númerico.")
print("O programa foi executado com Sucesso.")