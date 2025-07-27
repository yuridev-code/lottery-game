import customtkinter as ctk
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from interface.pagina_historico import HistoricoJanela

# Funções temporárias (mock)
def sortear_numeros_loteria():
    return {5, 12, 23, 30, 44, 60}

def verificar_acertos(numeros_usuario, numeros_sorteados):
    return numeros_usuario.intersection(numeros_sorteados)

def premiar_jogador(qtd_acertos):
    if qtd_acertos >= 6:
        print("Prêmio máximo!")
    elif qtd_acertos >= 4:
        print("Prêmio médio!")
    elif qtd_acertos == 3:
        print("Prêmio pequeno!")
    else:
        print("Sem prêmio.")

def registrar_operacao(numeros_usuario, numeros_sorteados):
    print("Operação registrada.")

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
        entrada_usuario = self.entrada.get()
        try:
            numeros_usuario = set(int(num.strip()) for num in entrada_usuario.split(",") if 1 <= int(num.strip()) <= 60)
            if len(numeros_usuario) != 6:
                self.resultado.configure(text="Você deve digitar exatamente 6 números válidos.")
                return
        except:
            self.resultado.configure(text="Entrada inválida. Use apenas números entre 1 e 60.")
            return

        numeros_sorteados = sortear_numeros_loteria()
        acertos = verificar_acertos(numeros_usuario, numeros_sorteados)

        registrar_operacao(numeros_usuario, numeros_sorteados)  # Salva em registro.txt

        resultado_texto = f"Números sorteados: {sorted(numeros_sorteados)}\n" \
                          f"Seus números: {sorted(numeros_usuario)}\n" \
                          f"Acertos: {sorted(acertos)}\n"
        self.resultado.configure(text=resultado_texto)

        premiar_jogador(len(acertos))  # Exibe mensagem no terminal

def abrir_pagina_sorteio(janela_anterior=None):
    if janela_anterior:
        janela_anterior.withdraw()
    app = SorteioApp()
    app.mainloop()
    
# Permite testar separadamente
if __name__ == "__main__":
    app = SorteioApp()
    app.mainloop()