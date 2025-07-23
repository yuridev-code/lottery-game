import random

def obter_numeros_usuario():
    """
    Solicita ao usuário que escolha 6 números únicos entre 1 e 60.
    Retorna um conjunto (set) dos números escolhidos.
    """
    numeros_usuario = set() # Usado para armazenar os números escolhidos pelo usuário, sem repetição.
    while len(numeros_usuario) < 6:
        try:
            numero = int(input("Escolha um número entre 1 e 60: "))
            if 1 <= numero <= 60:
                if numero not in numeros_usuario:
                    numeros_usuario.add(numero)
                else:
                    print("Você já escolheu esse número. Digite outro número.")
            else:
                print("Por favor, escolha um número válido (entre 1 e 60).")
        except ValueError:
            print("Entrada inválida. Por favor, digite um número.")
    return numeros_usuario

def sortear_numeros_loteria():
    """
    Gera 6 números aleatórios únicos para o sorteio da loteria.
    Retorna um conjunto (set) dos números sorteados.
    """
    return set(random.sample(range(1, 61), 6))

def verificar_acertos(numeros_usuario, numeros_sorteados):
    """
    Compara os números do usuário com os números sorteados e
    retorna um conjunto dos números que correspondem (acertos).
    """
    return numeros_usuario.intersection(numeros_sorteados)

def exibir_resultados(numeros_usuario, numeros_sorteados, numeros_acertados):
    """
    Exibe os números do usuário, os números sorteados e os números acertados.
    """
    print(f"\nNúmeros sorteados: {sorted(numeros_sorteados)}")
    print(f"Seus números: {sorted(numeros_usuario)}")
    print(f"Você acertou {len(numeros_acertados)} número(s): {sorted(numeros_acertados)}")
    
    
        

def premiar_jogador(quantidade_acertos):
    """
    Determina e imprime o prêmio com base na quantidade de acertos.
    """
    if quantidade_acertos < 3:
        print("Infelizmente você não ganhou nenhum prêmio.")
    elif quantidade_acertos == 3:
        print("Você ganhou um prêmio por acertar 3 números!")
    elif quantidade_acertos == 4:
        print("Você ganhou um prêmio por acertar 4 números!")
    elif quantidade_acertos == 5:
        print("Você ganhou um prêmio por acertar 5 números!")
    elif quantidade_acertos == 6:
        print("Parabéns!! Você ganhou o prêmio máximo por acertar 6 números!")
    return quantidade_acertos

def main():
    """
    Função principal para executar o jogo da loteria.
    """
    numeros_escolhidos_pelo_usuario = obter_numeros_usuario()
    numeros_sorteados_loteria = sortear_numeros_loteria()
    
    numeros_que_correspondem = verificar_acertos(numeros_escolhidos_pelo_usuario, numeros_sorteados_loteria)
    
    exibir_resultados(numeros_escolhidos_pelo_usuario, numeros_sorteados_loteria, numeros_que_correspondem)
    premiar_jogador(len(numeros_que_correspondem))


    