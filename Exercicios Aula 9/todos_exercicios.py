print("1. Exercício 1")
print("2. Exercício 2")
print("3. Exercício 3")
print("4. Exercício 4")
print("5. Exercício 5")
print("6. Exercício 6")
print("7. Exercício 7")
print("8. Exercício 8")

exercicio = int(input("Digite o número do exercício: "))

if exercicio == 1:

    print("-- Exercício 1 --")

    laboratorio = float(input("Digite a nota de trabalho de laboratório: "))
    avaliacao = float(input("Digite a nota da avaliação semestral: "))
    exame = float(input("Digite a nota do exame final: "))

    media = laboratorio * 0.2 + avaliacao * 0.3 + exame * 0.5

    print("A média é de {:.1f}" .format(media))

    if media >= 8:
        print("Conceito A")

    elif media >= 7:
        print("Conceito B")

    elif media >= 6:
        print("Conceito C")

    elif media >= 5:
        print("Conceito D")

    else:
        print("Conceito D")

elif exercicio == 2:

    print("-- Exercício 2 --")

    numero1 = int(input("Digite o primeiro número: "))
    numero2 = int(input("Digite o segundo número: "))

    if numero1 > numero2:
        print(numero1, "é o numero maior. Ou seja, primeiro número")

    else:
        print(numero2, "é o numero maior. Ou seja, segundo número")

elif exercicio == 3:

    print("-- Exercício 3 --")

    numero1 = float(input("Digite o primeiro número: "))
    numero2 = float(input("Digite o segundo número: "))
    numero3 = float(input("Digite o terceiro número: "))

    if numero1 > numero2 and numero1 > numero3:
        print(numero1)

        if numero2 > numero3:
            print(numero2)
            print(numero3)
        else:
            print(numero3)
            print(numero2)

    elif numero2 > numero1 and numero2 > numero3:
        print(numero2)

        if numero1 > numero3:
            print(numero1)
            print(numero3)
        else:
            print(numero3)
            print(numero1)

    else:
        print(numero3)

        if numero1 > numero2:
            print(numero1)
            print(numero2)
        else:
            print(numero2)
            print(numero1)

elif exercicio == 4:

    print("-- Exercício 4 --")

    numero1 = int(input("Digite o primeiro número: "))
    numero2 = int(input("Digite o segundo número: "))
    numero3 = int(input("Digite o terceiro número: "))

    if numero1 == numero2 and numero2 == numero3:
        print("Os três números digitados são iguais.")

    elif numero1 > numero2 and numero1 > numero3:
        print(numero1)

        if numero2 > numero3:
            print(numero2)
            print(numero3)
        else:
            print(numero3)
            print(numero2)

    elif numero2 > numero1 and numero2 > numero3:
        print(numero2)

        if numero1 > numero3:
            print(numero1)
            print(numero3)
        else:
            print(numero3)
            print(numero1)

    else:
        print(numero3)

        if numero1 > numero2:
            print(numero1)
            print(numero2)
        else:
            print(numero2)
            print(numero1)

elif exercicio == 5:

    print("-- Exercício 5 --")

    numero1 = int(input("Digite o primeiro número: "))
    numero2 = int(input("Digite o segundo número: "))
    numero3 = int(input("Digite o terceiro número: "))

    if numero1 <= numero2 and numero2 <= numero3:
        print("Os numeros foram digitados em ordem crescente")

    else:
        print("Os números não foram digitados em ordem crescente")

elif exercicio == 6:

    print("-- Exercício 6 --")

    numero = int(input("Digite o número: "))

    if numero % 2 == 0:
        print(numero, "é um número par.")

    else:
        print(numero, "é uma número impar.")

elif exercicio == 7:

    print("-- Exercício 7 --")

    numero = int(input("Digite o número: "))

    if numero % 5 == 0 and numero % 10 == 0:
        print(numero, "é múltiplo de 5 e de 10")

    else:
        print(numero, "não é múltiplo de 5 e de 10")

elif exercicio == 8:

    print("-- Exercício 8 --")

    numero1 = float(input("Digite o primeiro número: "))
    numero2 = float(input("Digite o segundo número: "))

    soma = numero1 + numero2

    print("A soma de {} e {}, é igual a {}" .format(numero1, numero2, soma))

    if soma > 10:
        print("Número maior que 10")

    else:
        print("Número menor ou igual a 10")
