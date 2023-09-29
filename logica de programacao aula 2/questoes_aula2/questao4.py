letra = str(input("Digite uma letra: "))
vogal = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']

if letra in vogal:
    print(f'a letra "{letra}" é uma vogal.')
else:
    print(f'a letra "{letra}" é uma consoante.')



letra = str(input("Digite uma letra: "))

if letra in "aeiouAEIOU":
    print(f'a letra "{letra}" é uma vogal.')
else:
    print(f'a letra "{letra}" é uma consoante.')