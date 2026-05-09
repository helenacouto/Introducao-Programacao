matriz = [[None]*3 for x in range(3)]
for i in range(3):
    for j in range(3):
        matriz[i][j] = int(input(f"Valor da linha {i + 1}, coluna {j + 1}: "))

for i in range(3):
    troca = matriz[1][i]
    matriz[1][i] = matriz[i][1]
    matriz[i][1] = troca
print(matriz)

