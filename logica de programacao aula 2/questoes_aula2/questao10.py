var1 = str(input("Qual turno do curso? Digite M para matutino, V para vespertino e N para noturno. "))

if var1 in 'mM':
    print("Bom dia!")
elif var1 in 'tT':
    print("Boa tarde!")
elif var1 in 'nN':
    print("Boa noite!")
else:
    print("Valor inválido.")