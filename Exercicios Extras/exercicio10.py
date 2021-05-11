print("1. Somar dois números")
print("2. Raiz quadrada de um número")
escolha = int(input("Digite a opção desejada (1/2): "))

if escolha == 1:
    num1 = int(input("Digite o primeiro número: "))
    num2 = int(input("Digite o segundo número: "))
    soma = num1 + num2
    print("O valor da soma é: ", soma)

else:
    num1 = int(input("Digite o número: "))
    raiz = float(num1) ** 0.5
    print("O valor da Raiz quadrada: {:.0f} " .format(raiz))
