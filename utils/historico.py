def historico(sorteio, aposta, acertos, numeros_acertados):
    with open("dados/historico.txt", 'a') as f:
        f.write(f"Sorteio: {sorteio} | Aposta: {aposta} | Acertos: {acertos} | Números Acertados: {numeros_acertados}\n")

