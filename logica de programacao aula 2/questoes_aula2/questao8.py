Arezzo = float(input("Qual valor da bolsa Arezzo? "))
Schutz = float(input("Qual valor da bolsa Schutz? "))
Kipling = float(input("Qual valor da bolsa Kipling? "))

if Arezzo <= Schutz and Arezzo <= Kipling:
    print(f"Você deverá comprar a bolsa Arezzo, que custa R${Arezzo}.")
elif Schutz <= Arezzo and Schutz <= Kipling:
    print(f"Você deverá comprar a bolsa Schutz, que custa R${Schutz}.")
elif Kipling <= Arezzo and Kipling <= Schutz:
    print(f"Você deverá comprar a bolsa Kipling, que custa R${Kipling}.")

