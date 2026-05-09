while True:
    frase = input("Digite uma frase (-1 para sair): ")
    if frase == "-1":
        break

    dicionario = {}
    for i in range(len(frase)):
        caractere = frase[i]

        if caractere in dicionario:
            dicionario[caractere] += 1
        else:
            dicionario[caractere] = 1

    print(f"Dicionario: {dicionario}")