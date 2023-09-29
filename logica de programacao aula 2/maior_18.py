nome = str(input("Digite seu nome: "))
idade = int(input("Digite sua idade: "))


if idade >= 18:
    print(f"Você, {nome}, já é de maior")
else:
    print(f"Você, {nome}, ainda é de menor")