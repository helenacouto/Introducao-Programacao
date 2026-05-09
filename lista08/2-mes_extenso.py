def extenso_mes(num):
    meses = [
        "janeiro", "fevereiro", "março", "abril", "maio", "junho",
        "julho", "agosto", "setembro", "outubro", "novembro", "dezembro"
    ]

    return meses[num - 1]


def main():
    data = input("Data de nascimento(dd/mm/aaa): ")
    
    dia, mes, ano = data.split("/")
    print(f"Data por extenso: {dia} de {extenso_mes(int(mes))} de {ano}.")


if (__name__ == "__main__"):
    main()