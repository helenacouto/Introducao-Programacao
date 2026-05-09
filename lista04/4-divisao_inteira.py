n1 = int(input("Digite um numero: "))
n2 = int(input("Digite outro numero: "))
inteiro = 0

while n1 - n2 >= 0:
    n1 = n1 - n2
    inteiro = inteiro + 1

print(f"Divisao inteira do primeiro pelo segundo: {inteiro}\nResto da divisao: {n1}")