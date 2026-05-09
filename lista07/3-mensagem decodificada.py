codigo = {0: " "}
alfabeto = "abcdefghijklmnopqrstuvwxyz"
for i in range(26):
    codigo[i + 1] = alfabeto[i]

mensagem = []
num = 0
while num != -1:
    num = int(input("Digite a mensagem por codigo(-1 para sair): "))
    if num != -1:
        mensagem.append(num)

final = ""
for i in range(len(mensagem)):
    final += codigo[mensagem[i]]

print(f"Mensagem decodificada: {final}.")

