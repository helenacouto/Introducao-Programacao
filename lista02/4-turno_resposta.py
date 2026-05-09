turno = input("Qual turno voce estuda?\n(M) Matutino\n(V) Vespertino\n(N) Noturno\n")

if turno == "M":
    print("Bom dia!")
elif turno == "V":
    print("Boa tarde!")
elif turno == "N":
    print("Boa noite!")
else:
    print("Resposta invalida.")