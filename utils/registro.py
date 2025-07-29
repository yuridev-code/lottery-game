def registro(data_hora, aposta, sorteio, acertos, numeros_acertados):
    with open("dados/sorteios.txt", 'a') as f:
        f.write(f"{data_hora} - Sorteio: {sorteio}\n")
    with open("dados/apostas.txt", 'a') as f:
        f.write(f"{data_hora} - Aposta: {aposta}\n")
