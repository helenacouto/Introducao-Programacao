x = 70000
y = 180000
anos = 0

while x < y:
    x = x + (x * 0.035)
    y = y + (y * 0.015)
    anos = anos + 1

print(f"Vai demorar {anos} anos.")
