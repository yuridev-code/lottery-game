    
        #========Função gerar sorteio========   

import random

def gerar_sorteio():

    return set(random.sample(range(1, 61), 6))

#Observação: Irá gerar 6 numeros aleatórios únicos para o sorteio da loteria de 1 a 60.