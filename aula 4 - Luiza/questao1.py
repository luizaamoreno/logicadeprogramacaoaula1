while True:
    aluno = str(input("Digite o nome do aluno: "))
    if aluno == 'fim':
        break
    nota = float(input("Digite a nota do aluno na disciplina: "))

    if nota > 10:
        print("Esta nota é inválida. Digite um número entre 0 e 10.")
    elif nota < 0: 
        print("Esta nota é inválida. Digite um número entre 0 e 10.")
    else:
        print("Nota válida. Próximo aluno ->")
        continue
