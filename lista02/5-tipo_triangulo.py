L1 = float(input("Digite o comprimento de um lado de um triangulo: "))
L2 = float(input("Digite o comprimento de outro lado: "))
L3 = float(input("Digite o comprimento de outro lado: "))

if L1 == L2 == L3:
    print("Esse triangulo eh equilatero.")
elif L1 == L2 != L3 or L1 == L3 != L2 or L2 == L3 != L1:
    print("Esse triangulo eh isosceles.")
elif L1 != L2 != L3:
    print("Esse triangulo eh escaleno.")