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
