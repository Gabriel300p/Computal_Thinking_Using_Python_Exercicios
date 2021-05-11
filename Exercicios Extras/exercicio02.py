num1 = int(input("Digite o primeiro número:	"))
num2 = int(input("Digite o segundo número: "))

divisao = num1 % num2

if divisao >= 1:
    print("O primeiro número não é divisível pelo segundo número")

else:
    print("O primeiro número é divisível pelo segundo número")
