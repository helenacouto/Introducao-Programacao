def main():
    frase = input("Digite: ").split()
    
    frase2 = "".join(frase)
    print(f"String sem os brancos: {frase2}")

if (__name__ == "__main__"):
    main()