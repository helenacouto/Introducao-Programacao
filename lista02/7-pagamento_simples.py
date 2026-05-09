valor = float(input("Digite o valor da compra: "))
pag = input("Qual a forma de pagamento? (Dinheiro ou Cheque): ")

if valor >= 100 and pag == "Dinheiro":
    print(f"Valor final a pagar: R$ {valor - valor / 10:.2f}")
elif pag == "Dinheiro" or pag == "Cheque":
    print(f"Valor final a pagar: R$ {valor:.2f}")
else:
    print("Forma de pagamento invalida.")