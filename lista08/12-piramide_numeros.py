def funcao(n):
    for i in range(1, n+1):
        print((str(i) + " ") * i)

def main():
    n = int(input("Digite um valor inteiro: "))
    funcao(n)

if (__name__ == "__main__"):
    main()