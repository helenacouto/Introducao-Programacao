valor = float(input("Digite o valor da compra: "))
pag = input("Forma de pagamento (Dinheiro ou Cheque ou Cartao): ")

if pag == "Cartao":
    cartao = input("Debito ou Credito? ")
    if cartao == "Credito":
        parcelas = int(input("Quantidade de parcelas (limite de ate 3 vezes): "))
        
if valor >= 100 and pag == "Dinheiro":
    print(f"O valor final a pagar: R$ {valor - valor / 10:.2f}")
elif pag == "Dinheiro" or pag == "Cheque" or cartao == "Debito":
    print(f"O valor final a pagar: R$ {valor:.2f}")
elif cartao == "Credito" and parcelas <= 3:
    print(f"O valor final a pagar eh: R$ {valor:.2f}\nEm {parcelas} parcela(s) de R${valor / parcelas:.2f}.")
elif cartao == "Credito" and parcelas > 3:
    print("Quantidade de parcelas invalida.")
else:
    print("Invalido")