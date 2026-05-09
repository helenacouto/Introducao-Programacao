n = int(input("Ha quantas pessoas na turma? "))

soma = 0
for i in range(n):
    idade = int(input("Qual a sua idade? "))
    soma += idade

media = soma / n
if media <= 25:
    print("A turma eh jovem.")
elif media <= 60:
    print("A turma eh adulta.")
else:
    print("A turma eh idosa.")