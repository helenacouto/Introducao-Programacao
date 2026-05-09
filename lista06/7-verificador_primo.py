num = int(input("Numero para verificar se eh primo: "))

primo = 0
for i in range (2, num):
    if num % i == 0:
        primo = 1

if primo == 1 or num == 0 or num == 1:
    print(f"O numero {num} nao eh primo.")
elif primo == 0 or num == 2:
    print(f"O numero {num} eh primo.")