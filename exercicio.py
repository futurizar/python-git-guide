nome = input("Seu nome: ")
idade = int(input("Sua idade: "))
if idade < 18:
    print(f"{nome}, você é jovem demais para bugs!")
else:
    print(f"{nome}, bem-vindo ao clube dos mestres do código!")
for i in range(idade):
    print(f"Ano {i+1} de sabedoria tech!")