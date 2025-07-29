import datetime
from utils.sorteio import gerar_sorteio
from utils.comparacao import comparar_apostas
from utils.registro import registro
from utils.historico import historico
from utils.validacao import validar_aposta

def fazer_aposta_e_sortear(entry_numeros, labels_dict):
    aposta = validar_aposta(entry_numeros)
    if aposta is None:
        return

    sorteio = gerar_sorteio()
    acertos, numeros_acertados = comparar_apostas(sorteio, aposta)

    labels_dict["sorteio"].configure(text=f"Números Sorteados: {sorteio}")
    labels_dict["aposta"].configure(text=f"Sua Aposta: {aposta}")
    labels_dict["acertos"].configure(text=f"Você acertou {acertos} número(s)")
    labels_dict["numeros_acertados"].configure(
        text=f"Números Acertados: {numeros_acertados}" if acertos else "Números Acertados: Nenhum"
    )

    data_hora = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    registro(data_hora, aposta, sorteio, acertos, numeros_acertados)
    historico(sorteio, aposta, acertos, numeros_acertados)
