num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))

cont1 = 0

if num1 > num2:
    aux = num1
    num1 = num2
    num2 = aux

for cont in range(num1 + 1, num2):
    if cont % 2 != 0:
        cont1 += 1

print("A quantidade de número pares é: ", cont1)
