num1 = int(input("digite o 1º número: "))
num2 = int(input("digite o 2º número: "))
num3 = int(input("digite o 3º número: "))

if num1 > num2 and num1 > num3:
    print(f"Entre os números digitados, o maior é {num1}.")
elif num2 > num1 and num2 > num3:
    print(f"Entre os números digitados, o maior é {num2}.")
elif num3 > num1 and num3 > num2:
    print(f"Entre os números digitados, o maior é {num3}.")

