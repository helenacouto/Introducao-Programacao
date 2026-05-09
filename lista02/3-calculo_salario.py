salario = float(input("Quanto que voce ganha por hora? "))
horas = float(input("E quantas horas voce trabalha no mes? "))

sal_bruto = salario * horas
imp_renda = 11/100 * sal_bruto
inss = 8/100 * sal_bruto
sindicato = 5/100 * sal_bruto
sal_liquido = sal_bruto - imp_renda - inss - sindicato

print(f"""Salario bruto: R${sal_bruto:.2f}
IR (11%): R${imp_renda:.2f}
INSS (8%): R${inss:.2f}
Sindicato (5%): R${sindicato:.2f}
Liquido: R${sal_liquido:.2f}""")