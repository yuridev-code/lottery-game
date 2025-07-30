from datetime import datetime

def historico(sorteio, aposta, acertos, numeros_acertados):
    data_hora = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    with open("dados/historico.txt", 'a', encoding="utf-8") as f:
        f.write(f"{data_hora} Sorteio: {sorteio} | Aposta: {aposta} | Acertos: {acertos} | Números Acertados: {numeros_acertados}\n")

