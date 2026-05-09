num1 = 1
num2 = 0

while num1 != 500:
    if num1 % 3 == 0 and num1 % 2 != 0:
        num2 = num2 + num1
        num1 = num1 + 1
    else:
        num1 = num1 + 1
print(num2)