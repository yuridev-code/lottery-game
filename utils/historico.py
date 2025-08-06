
def historico(data_hora, id, sorteio, aposta, acertos, numeros_acertados):
    """Registra dados da aposta em arquivo de histórico.txt."""
    if acertos == 0:
        numeros_acertados_str = "Nenhum"
    else:
        numeros_acertados_str = ", ".join(map(str, numeros_acertados))

    with open("dados/historico.txt", 'a', encoding="utf-8") as f:
        f.write("\n" + "="*63 + "\n")
        f.write(f" Data/Hora        : {data_hora}\n")
        f.write(f" ID               : {id}\n")
        f.write(f" Números Sorteados: {', '.join(map(str, sorteio))}\n")
        f.write(f" Sua Aposta       : {', '.join(map(str, aposta))}\n")
        f.write(f" Acertos          : {acertos}\n")
        f.write(f" Números Acertados: {numeros_acertados_str}\n")