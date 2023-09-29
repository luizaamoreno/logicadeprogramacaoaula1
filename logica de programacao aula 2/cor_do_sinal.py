sinal = str(input("digite uma cor do sinal"))

if sinal == "vermelho":
    print("Pare")
elif sinal == "amarelo":
    print("reduza e atenção")
elif sinal == "verde":
    print("Continue")
else:
    print("As cores válidas são vermelho, amarelo e verde. Digite uma cor válida.")