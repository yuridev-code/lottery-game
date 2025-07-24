def comparar_apostas(numeros_usuario, numeros_sorteados):

    acertos = set(numeros_usuario).intersection(numeros_sorteados)
    numeros_sorteados = len(acertos)
    return acertos, numeros_acertados