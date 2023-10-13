import random

lista_clientes = []

while True:
    nome = str(input("Digite seu nome: "))
    if nome == "fim" or "FIM":
        break
    telefone = str(input("Digite seu telefone: "))
    endereco = str(input("Digite seu endereço: "))
    lista_clientes.append([nome, telefone, endereco])
    
sorteado = random.choice(lista_clientes)
print(f"O cliente sorteado foi o {sorteado[0]}.")