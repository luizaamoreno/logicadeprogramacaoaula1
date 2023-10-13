#senha contendo obrigatoriamente letra e número e > 8 caracteres

alfabeto = 'abcdefghijklmnopqrstuvwxyz'
algarismos = '0123456789'

# while True:
#     senha = str(input("Digite uma senha: "))

#     for letra in senha: #loop para varrer o que o usuário digitar em senha
#         if letra in algarismos:
#             print("tem número")
#         elif letra in alfabeto: 
#             print("tem letra.")
#         else:
#             break


while True:
    senha = str(input("Digite uma senha: "))
    tem_letra = False
    tem_numero = False

    for letra in senha: #loop para varrer o que o usuário digitar em senha
        if letra in algarismos:
            tem_numero = True
        elif letra in alfabeto: 
            tem_letra = True
    if tem_letra == True and tem_numero == True and len(senha) >= 8:
        print("senha válida")
        break
    else:
        print("senha inválida.")
