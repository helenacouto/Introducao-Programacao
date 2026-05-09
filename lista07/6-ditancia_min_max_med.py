N = int(input("Quantos pontos deseja inserir? "))

pontos = []
for i in range(N):
    x = float(input(f"Digite o x do ponto {i+1}: "))
    y = float(input(f"Digite o y do ponto {i+1}: "))
    pontos.append((x, y))

distancias = []
for i in range(len(pontos)):
    for j in range(i + 1, len(pontos)):
        x1 = pontos[i][0]
        y1 = pontos[i][1]
        x2 = pontos[j][0]
        y2 = pontos[j][1]

        distancia = ((x2 - x1)**2 + (y2 - y1)**2) ** 0.5
        distancias.append(distancia)


maior = distancias[0]
menor = distancias[0]
soma = 0
for i in range(len(distancias)):
    if distancias[i] > maior:
        maior = distancias[i]
    if distancias[i] < menor:
        menor = distancias[i]
    soma += distancias[i]

media = soma / len(distancias)
print(f"Distância mínima: {menor:.2f}")
print(f"Distância máxima: {maior:.2f}")
print(f"Distância média: {media:.2f}")