numero = int(input("Digite um número: "))

if numero == 0:
    print("este é um número neutro")
elif numero > 0:
    print("este é um número positivo")
else:
    print("este é um número negativo")



numero = int(input("Digite um número: "))

if numero > 0:
    print(f"O número {numero} é positivo")
elif numero < 0:
    print(f"O número {numero} é negativo")
else:
    print(f"O número {numero} é neutro")