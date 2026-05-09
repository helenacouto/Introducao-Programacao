def soma(n1, n2, n3):
    todos = n1 + n2 + n3
    return todos

def main():
    num1 = int(input("Digite um valor inteiro: "))
    num2 = int(input("Digite outro valor inteiro: "))
    num3 = int(input("Digite outro valor inteiro: "))

    print(f"A soma dos três valores eh {soma(num1, num2, num3)}.")

if __name__ == "__main__":
    main()