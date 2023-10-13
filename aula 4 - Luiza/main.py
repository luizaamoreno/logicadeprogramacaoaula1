# #WHILE:

# contador = 0
# while contador < 10:
#     print(contador)
#     contador = contador + 1

contador = 0
while contador < 20:
    print(contador)
    contador = contador + 2

while True:
    nome = str(input("Digite seu nome: "))

    if nome == "sair":
        print("Tchau")
        break