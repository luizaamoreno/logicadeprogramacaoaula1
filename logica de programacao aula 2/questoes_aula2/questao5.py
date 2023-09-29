nota1 = float(input("Nota de matemática: "))
nota2 = float(input("Nota de português: "))

media = ((nota1+nota2)/2)
print(f"A média das notas é {media}.")

if media >= 7.0 and media < 10.0:
    print("O aluno está aprovado.")
elif media == 10.0:
    print("O aluno está aprovado com distinção.")
else:
    print("O aluno está reprovado.")
