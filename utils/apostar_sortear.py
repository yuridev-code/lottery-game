import datetime
from utils.definido import definido
from utils.sorteio import gerar_sorteio
from utils.comparacao import comparar_apostas
from utils.historico import historico
from utils.validacao import validar_aposta
from utils.gerar_id import gerar_id


def _exibir_resultado(labels_dict, id, sorteio, aposta, acertos, numeros_acertados, acertos_totais):
    if acertos_totais < 4:
        mensagem = "VOCÊ PERDEU MIZERAVI!!!"
    elif acertos_totais == 4:
        mensagem = "PARABÉNS, VOCÊ FEZ UMA QUADRA MIZERAVI!!!"
    elif acertos_totais == 5:        
        mensagem = "PARABÉNS, VOCÊ FEZ UMA QUINA MIZERAVI!!!"         
    else:
        mensagem = "VOCÊ GANHOU O PRÊMIO MÁXIMO SEU MIZERAVI!!!"

    labels_dict["resultado"].configure(text=mensagem)
    labels_dict["id"].configure(text=f"O seu ID: {id}")
    labels_dict["sorteio"].configure(text=f"Números Sorteados: {sorteio}")
    labels_dict["aposta"].configure(text=f"Sua Aposta: {aposta}")
    labels_dict["acertos"].configure(text=f"Você acertou {acertos} número(s)")
    
    if acertos:
        numeros_str = f"Números Acertados: {numeros_acertados}"
    else:
        numeros_str = "Números Acertados: Nenhum"
    labels_dict["numeros_acertados"].configure(text=numeros_str)


def _registrar_historico(id, sorteio, aposta, acertos, numeros_acertados):
    data_hora = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    historico(data_hora, id, sorteio, aposta, acertos, numeros_acertados)


def fazer_aposta_e_sortear(entry_numeros, labels_dict):
    aposta = validar_aposta(entry_numeros)
    if aposta is None:
        return

    id = gerar_id()
    sorteio = gerar_sorteio()
    acertos, numeros_acertados = comparar_apostas(sorteio, aposta)
    acertos_totais = len(set(sorteio) & set(aposta))

    _exibir_resultado(labels_dict, id, sorteio, aposta, acertos, numeros_acertados, acertos_totais)
    _registrar_historico(id, sorteio, aposta, acertos, numeros_acertados)


def banca_doida(entry_numeros, labels_dict):
    aposta = validar_aposta(entry_numeros)
    if aposta is None:
        return

    id = gerar_id()
    sorteio = definido()
    acertos, numeros_acertados = comparar_apostas(sorteio, aposta)
    acertos_totais = len(set(sorteio) & set(aposta))

    _exibir_resultado(labels_dict, id, sorteio, aposta, acertos, numeros_acertados, acertos_totais)
    _registrar_historico(id, sorteio, aposta, acertos, numeros_acertados)
