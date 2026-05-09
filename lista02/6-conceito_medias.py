nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
media = (nota1 + nota2) / 2

if media <= 10 and media >= 9:
    print("Conceito A")
elif media < 9 and media >= 7.5:
    print("Conceito B")
elif media < 7.5 and media >= 6:
    print("Conceito C")
elif media < 6 and media >= 4:
    print("Conceito D")
elif media < 4 and media >= 0:
    print("Conceito E")