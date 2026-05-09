codigo = int(input("Digite o codigo do produto (0 para sair): "))
qntd = int(input("Quantidade deste produto comprada: "))
total = 0

while codigo != 0:
    if codigo == 1:
        total = total + 5.50 * qntd
    elif codigo == 2:
        total = total + 2.30 * qntd
    elif codigo == 3:
        total = total + 4.75 * qntd
    elif codigo == 4:
        total = total + 6.80 * qntd
    elif codigo == 5:
        total = total + 9.30 * qntd
    else:
        print("Codigo invalido")
        
    codigo = int(input("\nDigite o codigo do proximo produto (0 para sair): "))
    qntd = int(input("Quantidade deste produto comprada: "))

print(f"\nTotal a pagar: R${total:.2f}")