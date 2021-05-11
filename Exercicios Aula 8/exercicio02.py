print("Destinos: Norte, Nordeste ou Centro-Oeste.")

destino = input("Qual o destino? ")

if destino == "Norte" or destino == "norte":

    norte = int(input("Para Ida digite 1, para ida e volta digite 2: "))

    if norte == 1:
        print("")
    elif norte == 2:
        print("Para ida e volta, fica no valor de R$400,00")
    else:
        print("Argumentos inválidos")

elif destino == "Nordeste" or destino == "nordeste":

    nordeste = int(input("Para Ida digite 1, para ida e volta digite 2: "))

    if nordeste == 1:
        print("Para apenas ida, fica no valor de R$380,00")
    elif nordeste == 2:
        print("Para ida e volta, fica o valor de R$628,00")
    else:
        print("Argumentos ivalidos")

elif destino == "Centro-Oeste" or destino == "centro-oeste":

    centro_oeste = int(input("Para Ida digite 1, para ida e volta digite 2: "))

    if centro_oeste == 1:
        print("Para apenas ida, fica no valor de R$620,00")
    elif centro_oeste == 2:
        print("Para ida e volta, fica o valor de R$1100,00")
    else:
        print("Argumentos ivalidos")

else:
    print("Por favor, digite um valor valido.")
    print("Obs: Não trabalhamos nos trechos sul e suldeste")
