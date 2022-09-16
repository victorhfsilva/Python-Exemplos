#While Loop
n = 10
lista = []
while n>0:
    lista.append(n)
    n=n-1
print(lista)

lista.clear()
while n<10:
    n=n+1
    lista.append(n)
print(lista,"\n")

#Breaks
x0 = 1
x1 = 1
i = 0
def proximoFibonacci():
    if i>1:
        global x0, x1
        res = x0+x1
        print(res)
        x0 = x1
        x1 = res
    elif i == 0:
        print(x0)
    elif i == 1:
        print(x1)
        
while True:
    continuar = input("Deseja saber o próximo número de Fibonacci? [Y/N]")
    if continuar == "Y" or continuar == "y":
        proximoFibonacci()
        i=i+1
    elif continuar == "N" or continuar == "n":
        break
print("Sequência finalizada")


