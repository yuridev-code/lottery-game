import customtkinter as ctk
import os

DIRETORIO = "dados/historico.txt"

def abrir_historico():
    janela = ctk.CTkToplevel()
    janela.title("Histórico de Sorteios")
    janela.geometry("500x400")

    texto = ctk.CTkTextbox(janela, wrap='word')
    texto.pack(expand=True, fill="both", padx=10, pady=10)

    if os.path.exists(DIRETORIO):
        with open(DIRETORIO, 'r') as arquivo:
            conteudo = arquivo.read()
            texto.insert("0.0", conteudo)
    else:
        texto.insert("0.0", "Nenhum histórico encontrado.")