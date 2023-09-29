# num1 = int(input("digite um número: "))
# num2 = int(input("digite outro número: "))

# if num1 > num2:
#     print(f"{num1} é maior que {num2}.")
# else:
#     print(f"{num2} é maior que {num1}.")

num1 = int(input("digite um número: "))
num2 = int(input("digite outro número: "))

if num1 > num2:
    print(f"O primeiro número ({num1}) é maior que o segundo ({num2}).")
elif num2 > num1:
    print(f"O segundo número({num2}) é maior que o primeiro ({num1}).")
else:
    print("os números são iguais")