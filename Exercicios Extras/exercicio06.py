a = float(input("Digite o Primeiro número: "))
b = float(input("Digite o segundo número: "))
c = float(input("Digite o terceiro número: "))

if a == b and c == a and b == c:
    print("Triangulo Equilátero")

elif a == b or c == a or b == c:
    print("Triangulo isósceles")

elif a != b and a != c and c != b:
    print("Triangulo escaleno")
