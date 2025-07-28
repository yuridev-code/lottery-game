import customtkinter as ctk
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from interface.pagina_historico import HistoricoJanela
from utils.sorteio import gerar_sorteio
from utils.comparacao import comparar_apostas
from utils.registro import registro
from utils.exibicao import exibir
from utils.historico import historico

def premiar_jogador(qtd_acertos):
    if qtd_acertos >= 6:
        print("Prêmio máximo!")
    elif qtd_acertos >= 4:
        print("Prêmio médio!")
    elif qtd_acertos == 3:
        print("Prêmio pequeno!")
    else:
        print("Sem prêmio.")


ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("green")

class SorteioApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Sorteio Loteria")
        self.geometry("500x400")

        self.label_info = ctk.CTkLabel(self, text="Digite 6 números entre 1 e 60 (separados por vírgula):")
        self.label_info.pack(pady=10)

        self.entrada = ctk.CTkEntry(self, placeholder_text="ex: 5,12,23,35,42,60")
        self.entrada.pack(pady=10)

        self.botao_sortear = ctk.CTkButton(self, text="Sortear", command=self.realizar_sorteio)
        self.botao_sortear.pack(pady=10)

        self.resultado = ctk.CTkLabel(self, text="", wraplength=400)
        self.resultado.pack(pady=10)

        self.botao_historico = ctk.CTkButton(self, text="Ver Histórico", command=self.abrir_historico)
        self.botao_historico.pack(pady=5)

    def abrir_historico(self):
        HistoricoJanela()

    def realizar_sorteio(self):
        numeros_usuario = [
            int(self.entrada1.get()),
            int(self.entrada2.get()),
            int(self.entrada3.get()),
            int(self.entrada4.get()),
            int(self.entrada5.get()),
            int(self.entrada6.get())
        ]
        numeros_sorteados = gerar_sorteio()
        acertos, qtd_acertos = comparar_apostas(numeros_usuario, numeros_sorteados)

        registro(numeros_sorteados, numeros_usuario, qtd_acertos, acertos)
        historico(numeros_sorteados, numeros_usuario, qtd_acertos, acertos)
        exibir(numeros_sorteados, numeros_usuario, qtd_acertos, acertos)

def abrir_pagina_sorteio(janela_anterior=None):
    if janela_anterior:
        janela_anterior.withdraw()
    app = SorteioApp()
    app.mainloop()
    
# Permite testar separadamente
if __name__ == "__main__":
    app = SorteioApp()
    app.mainloop()