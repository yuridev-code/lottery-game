import random
from utils.constantes import *
def gerar_sorteio():
    """Gera uma lista ordenada de números únicos para o sorteio."""
    return sorted(random.sample(range(NUMERO_MINIMO_LOTERIA, NUMERO_MAXIMO_LOTERIA + 1), QUANTIDADE_NUMEROS_LOTERIA))
