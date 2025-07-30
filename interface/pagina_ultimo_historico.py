import os
import customtkinter as ctk

# pega o diretório raiz do projeto (uma pasta acima de interface)
DIR_RAIZ = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

# caminho absoluto para o arquivo historico.txt
DIRETORIO = os.path.join(DIR_RAIZ, 'dados', 'historico.txt')

def ultimo_historico():
    janela = ctk.CTkToplevel()
    janela.title("Último Sorteio")
    janela.geometry("500x400")

    texto = ctk.CTkTextbox(janela, wrap='word')
    texto.pack(expand=True, fill="both", padx=10, pady=10)

    if os.path.exists(DIRETORIO):
        with open(DIRETORIO, 'r', encoding='utf-8') as arquivo:
            conteudo = arquivo.read()
            texto.insert("0.0", conteudo)
    else:
        texto.insert("0.0", "Nenhum histórico encontrado.")
