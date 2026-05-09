n = float(input("Digite um número: "))
b = 2
p = (b + n / b) / 2

while abs(b - p) >= 0.0001:
    b = p
    p = (b + n / b) / 2
    
print(f"A raiz quadrada aproximada é {p}")
