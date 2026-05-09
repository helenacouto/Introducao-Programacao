def pos_neg(n):
    if n > 0:
        return "P"
    else:
        return "N"

def main():
    num = int(input("Digite um valor inteiro: "))
    print(pos_neg(num))

if __name__ == "__main__":
    main()