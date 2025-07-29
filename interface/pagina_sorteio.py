import customtkinter as ctk
from utils.apostar_sortear import fazer_aposta_e_sortear
from interface.pagina_historico import abrir_historico

class SorteioApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Sorteio Loteria")
        self.geometry("500x600")

        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("blue")

        self.label_info = ctk.CTkLabel(self, text="Digite 6 números entre 1 e 60:")
        self.label_info.pack(pady=10)

        self.entry_numeros = [ctk.CTkEntry(self, width=50, justify='center') for _ in range(6)]
        for entry in self.entry_numeros:
            entry.pack(pady=5)

        self.botao_sortear = ctk.CTkButton(self, text="Sortear", command=self.sortear)
        self.botao_sortear.pack(pady=10)

        self.labels_resultado = {
            "sorteio": ctk.CTkLabel(self, text=""),
            "aposta": ctk.CTkLabel(self, text=""),
            "acertos": ctk.CTkLabel(self, text=""),
            "numeros_acertados": ctk.CTkLabel(self, text="")
        }

        for label in self.labels_resultado.values():
            label.pack(pady=2)

        self.botao_historico = ctk.CTkButton(self, text="Ver Histórico", command=abrir_historico)
        self.botao_historico.pack(pady=10)

    def sortear(self):
        fazer_aposta_e_sortear(self.entry_numeros, self.labels_resultado)