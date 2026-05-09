altura = []
sexo = []
maior = 0
menor = 3
M = 0
F = 0
somaM = 0
somaF = 0

for i in range(10):
    altura.append(float(input(f"Qual a altura da {i + 1}° pessoa (em metros)? ")))
    sexo.append(input(f"Qual o sexo da {i + 1}° pessoa (M/F)? "))

    if altura[i] > maior:
        maior = altura[i]
        indice_maior = i


    if altura[i] < menor:
        menor = altura[i]
        indice_menor = i
    
    if sexo[i] == "M":
        somaM += altura[i]
        M += 1
    elif sexo[i] == "F":
        somaF += altura[i]
        F += 1

mediaM = somaM / M
mediaF = somaF / F

print(f"Ha {M} pessoa(s) do sexo masculino e a media de altura entre elas eh {mediaM:.2f}m.")
print(f"Ha {F} pessoa(s) do sexo feminino e a media de altura entre elas eh {mediaF:.2f}m.")
print(f"A maior altura registrada eh {altura[indice_maior]:.2f}m, pertencente a uma pessoa do sexo {sexo[indice_maior]}")
print(f"A menor altura registrada eh {altura[indice_menor]:.2f}m, pertencente a uma pessoa do sexo {sexo[indice_menor]}")
