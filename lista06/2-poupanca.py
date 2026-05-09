dep = float(input("Qual o valor do deposito? R$"))
juros = float(input("Qual eh a taxa de juros da poupança(em %)? "))

soma = dep
for i in range(1, 25):
    soma = soma + soma*(juros/100)
    print(f"{i}° mes: R${soma:.2f}")
    
print(f"Com o deposito inicial de R${dep:.2f}, acumulou-se R${soma:.2f} em 24 meses")