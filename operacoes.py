from colorama import init, Fore

init()  # Inicializa colorama

def soma(a, b):
    return a + b

def subtrai(a, b):
    return a - b

def multiplica(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ValueError(Fore.RED + "Erro: Divisão por zero!" + Fore.RESET)
    return a / b