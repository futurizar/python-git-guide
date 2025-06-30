import random

numero = random.randint(1, 10)
print(f"Dica: o número é entre 1 e 10!")
chute = int(input("Adivinhe um número de 1 a 10: "))
pontos = 100 if chute == numero else 0
if chute == numero:
    print("Acertou, mestre!")
else:
    print(f"Errou! Era {numero}.")
print(f"Pontuação: {pontos} pontos!")