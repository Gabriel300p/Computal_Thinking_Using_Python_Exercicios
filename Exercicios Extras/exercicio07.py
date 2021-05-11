nome = input("Qual o nome do aluno? ")
nota1 = float(input("Digite a primeria nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))
faltas = int(input("Digite o número de faltas: "))

media_nota = (nota1 + nota2 + nota3) / 3
media_falta = (faltas/80) * 100

if media_falta >= 25:
    print("Reprovado por falta")

else:
    if media_nota >= 7:
        print(nome, "esta provado!")
    else:
        print(nome, "esta reprovado!")
