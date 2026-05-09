valor = int(input("Digite um valor (-1 para sair): "))
menor = maior = valor
soma = 0

while valor != -1:
    if valor > maior:
        maior = valor
    elif valor < menor:
        menor = valor
    soma = soma + valor
    valor = int(input("Digite um valor (-1 para sair): "))

print(f"O maior valor eh {maior}, o menor valor eh {menor} e a soma de todos os valores eh {soma}.")