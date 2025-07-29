def comparar_apostas(sorteio, aposta):
    numeros_acertados = sorted(set(sorteio) & set(aposta))
    return len(numeros_acertados), numeros_acertados