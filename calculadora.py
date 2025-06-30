from operacoes import soma, subtrai, multiplica, divide

print(f"Soma: {soma(5, 3)}")
print(f"Subtração: {subtrai(5, 3)}")
print(f"Multiplicação: {multiplica(5, 3)}")
try:
    print(f"Divisão: {divide(6, 0)}")
except ValueError as e:
    print(e)