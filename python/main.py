nome_do_aluno = "Luiza" #tipo str
idade = 30 #tipo int
altura = 1.60 #tipo float
habilitacao = True #tipo bool
alemao = False #tipo bool

nota1 = 6
nota2 = 9
# string = "qualquer coisa aqui dentro"

# str é abreviatura de string
# int é abreviatura de número inteiro

print (nota1 + nota2)

print(nota1 == nota2) #igual a

print (nota1 != nota2) #diferente

print(nota1 // nota2) #divisao inteira

print(nota1 ** nota2) #nota1 elevado a nota 2

print(nota1 % nota2) #mostra o resto da divisão de um sobre o outro

print(nota1>nota2) #maior que ou menor que

print(nota1>=nota2) #maior ou igual

nome = str(input("Digite o seu nome: "))
idade = int(input("Digite a sua idade: "))
altura = float(input("Digite sua altura: "))

print(f"bem vindo {nome} sua idade é {idade} sua altura é {altura}")
#quando colocar o f antes e a variável dentro de chaves, ele já entende que é uma variável.
#f = format


