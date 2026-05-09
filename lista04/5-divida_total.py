divida = float(input("Qual o valor inicial da divida? "))
juros = float(input("Quanto eh o juros mensal? "))
pago_mensal = float(input("Qual o valor mensal que sera pago? "))

pago_total = 0
meses = 0
juros_total = 0

while divida > 0:
    juros_mensal = divida * juros
    divida = divida + juros_mensal - pago_mensal

    juros_total = juros_total + juros_mensal
    pago_total = pago_total + pago_mensal
    meses = meses + 1

print(f"A divida sera paga em {meses} meses. Total pago: R${pago_total:.2f}. Juros total: {juros_total:.2f}.")