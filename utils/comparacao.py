def comparar_apostas(sorteio, aposta):
    """Retorna a quantidade e os números acertados entre sorteio e aposta."""
    
    numeros_acertados = sorted(set(sorteio) & set(aposta))
    return len(numeros_acertados), numeros_acertados