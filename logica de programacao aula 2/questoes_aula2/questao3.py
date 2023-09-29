sexo = str(input("Sexo? [M | F]: "))

if sexo == "M" or sexo == "m":
    print("masculino")
elif sexo == "F" or sexo == "f":
    print("feminino")
else:
    print("sexo inválido")