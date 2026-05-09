n = int(input("Qual numero voce deseja ver a tabuada (1 a 10)? "))

print(f"Tabuada de {n}:\n")
for i in range(1, 11):
    print(f"{n} x {i} = {n*i}")