def rentabilidade(valorIni : float, taxaDeJuros : float):
    return valorIni * (1 + (taxaDeJuros / 100))

def calcula_porcentagem(valorIni : float, valorFinal : float):
    return ((valorFinal / valorIni) - 1)* 100