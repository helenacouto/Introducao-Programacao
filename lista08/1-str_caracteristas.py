def main():
    frase1 = input("String 1: ")
    frase2 = input("String 2: ")

    tam1 = len(frase1)
    tam2 = len(frase2)
    print(f"A string '{frase1}' possui {tam1} caracteres.")
    print(f"A string '{frase2}' possui {tam2} caracteres.")

    if (frase1 == frase2):
        print("As strings contem o mesmo conteudo.")
    else:
        print("As strings contem conteudos diferentes.")
    
    if (tam1 == tam2):
        print("As strings tem o mesmo comprimento.")
    else:
        print("As strings nao tem o mesmo comprimento.")

if (__name__ == "__main__"):
    main()