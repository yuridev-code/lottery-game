import customtkinter as ctk
import os


class HistoricoJanela(ctk.CTkToplevel):
    def __init__(self):
        super().__init__()
        self.title("Histórico de Jogos")
        self.geometry("600x400")

        self.texto = ctk.CTkTextbox(self, width=550, height=350)
        self.texto.pack(padx=20, pady=20)

        self.carregar_historico()

        # carrega o histórico
        try:
            with open("utils/historico.txt", "r", encoding="utf-8") as arquivo:
                conteudo = arquivo.read()
                self.texto.insert("1.0", conteudo)
        except FileNotFoundError:
            self.texto.insert("1.0", "Nenhum histórico encontrado.")

from utils.registro import registro
from utils.exibicao import exibir

registro([5, 12, 23, 30, 44, 60], [5, 12, 23, 30, 44, 60], 6, [5, 12, 23, 30, 44, 60])
exibir([5, 12, 23, 30, 44, 60], [5, 12, 23, 30, 44, 60], 6, [5, 12, 23, 30, 44, 60])