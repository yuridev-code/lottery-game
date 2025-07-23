# Implemente a solução aqui. 


# Definam e implementem todas as funções que julgarem necessárias.


                #5. Simulador de Loteria
# ● Descrição: Criar um simulador de loteria que sorteie números aleatórios e permita ao usuário
# verificar se os números escolhidos foram sorteados e realizar o registro da aposta.
# ● Funcionalidades (50 pontos):
# o Geração de números aleatórios para o sorteio (10 pontos).
# o Comparação dos números sorteados com os números escolhidos pelo usuário (10
# pontos).
# o Realizar registro das apostas e armazenar em um arquivo de texto (10 pontos).
# o Exibição dos resultados do sorteio e indicação de quantos números o usuário acertou (10
# pontos).
# o Armazenamento dos resultados em um arquivo de texto para futuras
# consultas/leituras/exibições (10 pontos).

import random

    # Aqui o Usuário escolhe/digita 6 numeros.
numero_usuario = set() # Essa linha será usada pra armazenar os números escolhidos pelo o usuario, sem repetição.

while len(numero_usuario) < 6:
    try:
        numero = int(input("Escolha um número entre 1 e 60: "))
        if numero < 1 or numero > 60:
            print("Por favor, escolha um número valido.")
        elif numero in numero_usuario:
            print("Você ja escolheu esse número. Digite outro número.")
        else:
            numero_usuario.add(numero)
    except ValueError:
        print("Por favor escolha um número válido.")

#Sorteia 6 números aleatórios.

sorteio_numeros = set(random.sample(range(1, 61), 6))
print(f"Números sorteados: {sorted(sorteio_numeros)}")
print(f"Seus números: {sorted(numero_usuario)}")


#Verifica quantos números o usuário acertou.
    
acertos = numero_usuario.intersection(sorteio_numeros)
numeros_acertados = len(acertos)
print (f"Você acertou {numeros_acertados} numero(s): {sorted(acertos)}")

    #Premiação
if numeros_acertados < 3:
    print("Infelizmente você não ganhou nenhum prêmio.")
elif numeros_acertados == 3:
    print("Você ganhou um prêmio por acertar 3 números!")
elif numeros_acertados == 4:
    print("Você ganhou um prêmio por acertar 4 números!")
elif numeros_acertados == 5:
    print("Você ganhou um prêmio por acertar 5 números!")
elif numeros_acertados == 6:
    print("Parabéns!! você ganhou  prêmio Maximo por acertar 6 números!")

# Armazenando dados no historico


