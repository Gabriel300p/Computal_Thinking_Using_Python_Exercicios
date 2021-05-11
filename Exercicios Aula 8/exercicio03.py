conta = int(input("Digite o valor da conta: "))

digito1 = conta // 100
digito2 = (conta % 100) // 10
digito3 = (conta % 100) % 10

inverso_str = str(digito3) + str(digito2) + str(digito1)
inverso_int = int(inverso_str)

soma_digito = conta + inverso_int

print("Soma da conta com inverso do numero é: ", soma_digito)

digito2 = soma_digito // 100
digito3 = (soma_digito % 100) // 10
digito4 = (soma_digito % 100) % 10

if soma_digito > 999:

    digito1 = soma_digito // 1000

    mult = digito1 * 1 + digito2 * 2 + digito3 * 3 + digito4 * 4
else:
    multiplicacao = digito2 * 1 + digito3 * 2 + digito4 * 3

codigo = multiplicacao % 10

print("O código verificador é: ", codigo)
