import random as r

aleatorio = r.randint(1,100)

numero = int(input("Digite um número entre 1 e 100: "))
while numero != aleatorio:
    if numero < aleatorio:
        print("Tente um número maior.")
    else:
        print("Tente um número menor.")
    numero = int(input("Digite um número entre 1 e 100: "))

print("Parabéns! Você acertou o número.")