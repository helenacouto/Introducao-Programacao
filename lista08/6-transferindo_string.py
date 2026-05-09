def main():
    stg = input("Digite uma string: ")
    i = 0 
    nova_stg = ""

    while i < len(stg):
        nova_stg = nova_stg + stg[i]
        i += 1
        print(nova_stg)

if(__name__ == "__main__"):
    main()