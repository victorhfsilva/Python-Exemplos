#Funções
def fatorial(n):
    if n == 1:
        return 1
    else: 
        return n*fatorial(n-1)

x_str = input("Insira um número inteiro.")
try:
    x = int(x_str)
    fatorial = fatorial(x)
    print("Fatorial de ",x,": ",fatorial)
except:
    print("Valor não númerico.")