def digitos(num):
    qntd = 1
    while (num > 10):
        num = num / 10
        qntd += 1
    return qntd

def main():
    n = int(input("Digite um numero inteiro: "))
    print(f"O numero {n} tem {digitos(n)} dígito(s).")

if (__name__ == "__main__"):
    main()