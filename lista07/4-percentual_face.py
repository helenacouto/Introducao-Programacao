import random

while True:
    n = int(input("Digite a quantidade de lancamentos (0 para sair): "))
    if n == 0:
        break

    faces = [0] * 6
    for i in range(n):
        resultado = random.randint(1, 6)
        faces[resultado - 1] += 1

    print("Percentual de cada face:")
    for i in range(len(faces)):
        percentual = (faces[i] / n) * 100
        print(f"Face {i + 1}: {percentual:.2f}%")
