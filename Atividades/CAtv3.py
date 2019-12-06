def calculaInvestimento(valor : float):
    preco = 104.10 * valor
    for i in range (0, 52):
        preco = preco * (1 + (0.41 / 100))

    return preco