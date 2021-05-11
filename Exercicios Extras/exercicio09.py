valor = int(input("Digite o valor do produto: "))

valor_20 = valor * 0.45
valor_20_mais = valor * 0.30

soma_20 = valor_20 + valor
soma_20_mais = valor_20_mais + valor


if valor <= 20:
    print("O valor do produto fica: ", soma_20)

else:
    print("O valor do produto fica: ", soma_20_mais)
