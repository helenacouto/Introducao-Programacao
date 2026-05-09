eleitores = int(input("Quantos eleitores? "))

lucas = 0
pedro = 0
joao = 0
for i in range(eleitores):
    print("DIGITE 01 - LUCAS\nDIGITE 02 - PEDRO\nDIGITE 03 - JOAO")
    voto = input("Seu voto: ")

    if voto == "01":
        lucas += 1
    elif voto == "02":
        pedro += 1
    elif voto == "03":
        joao += 1

print(f"Lucas recebeu {lucas} voto(s). Pedro recebeu {pedro} voto(s). Joao recebeu {joao} voto(s).")