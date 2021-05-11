numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))

soma = numero1 + numero2

print("A soma de {} e {}, é igual a {}" .format(numero1, numero2, soma))

if soma > 10:
    print("Número maior que 10")

else:
    print("Número menor ou igual a 10")
