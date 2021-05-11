salario = float(input("Qual o valor do Salário? "))

limite = salario * 0.30

emprestimo = float(input("Digite o valor da prestação: "))

if emprestimo > 0 and emprestimo <= salario:
    print("Emprestimo consedido!")

else:
    print("Emprestimo não consedido!")
