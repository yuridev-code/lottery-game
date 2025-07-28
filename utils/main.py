def main():
    # 1. Usuário escolhe os números
    aposta_do_usuario = escolher_numeros_usuario()

    # 2. Sorteia os números
    numeros_do_sorteio = gerar_sorteio()

    # 3. Compara as apostas
    numeros_acertados_set, contagem_acertos = comparar_apostas(aposta_do_usuario, numeros_do_sorteio)

    # 4. Exibe os resultados e premiação
    exibir_resultados(aposta_do_usuario, numeros_do_sorteio, numeros_acertados_set, contagem_acertos)

if __name__ == "__main__":
    main()