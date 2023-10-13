contador = 0
while True:
    #contador += 1
    contador = contador + 1
    if contador == 3:
        continue #essa função continue IGNORA O RESTANTE DO CÓDIGO, faz o código voltar pro começo, mesmo se tiver mais linhas de código embaixo.
    print(contador)
    if contador >= 10:
        break

#quando esse código é executado, ele pula o 3