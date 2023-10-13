#FAÇA UM PROGRAMA QUE PEDE PRO USUÁRIO DIGITAR UMA SENHA.
#SE A SENHA TIVER MENOS QUE 4 CARACTERES,  MOSTRE UMA MENSAGEM DE ERRO
#E PEÇA PARA ELE DIGITAR UMA SENHA VÁLIDA.
#SE A SENHA TIVER 8 CARACTERES OU MAIS, MOSTRE UMA MENSAGEM 
#NA TELA ESCRITO "SENHA VÁLIDA".



while True:
    senha = str(input("Digite uma senha para sua conta: "))

    if len(senha) < 8:
        print("Senha inválida. Tente novamente.")

    else:
        print("Senha válida.")
        break