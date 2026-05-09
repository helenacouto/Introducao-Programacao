base = int(input("Qual a base? "))
expo = int(input("Qual o expoente? "))

resultado = base
for i in range(expo - 1):
    resultado = resultado * base

print(resultado)
