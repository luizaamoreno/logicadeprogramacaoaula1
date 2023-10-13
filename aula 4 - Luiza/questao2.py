print("resolução Luiza: está comentada neste código")
# while True:
#     nome_de_usuario = str(input("Digite o seu login: "))
#     senha = str(input("Crie uma senha: "))

#     if senha == nome_de_usuario:
#         print("senha inválida. sua senha não pode ser igual ao nome de usuário.")
#     else:
#         print("senha válida.")
#         break

print("resolução do professor: ")
while True:
    nome_de_usuario = str(input("Digite o seu login: "))
    senha = str(input("Crie uma senha: "))

    if senha != nome_de_usuario:
        print("senha válida.")
    else:
        print("Senha inválida. Sua senha não pode ser igual ao nome de usuário.")
        break