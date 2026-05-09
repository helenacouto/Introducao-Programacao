elementos = int(input("Qual a quantidade de elementos? "))

atual = 1
antecessor = 0
antecessor2 = 0
for i in range(elementos):
    print(atual)
    antecessor2 = antecessor
    antecessor = atual
    atual =  antecessor + antecessor2
    