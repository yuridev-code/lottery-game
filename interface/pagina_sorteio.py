import customtkinter as ctk


# def exibir, def historico
def abrir_pagina_sorteio(janela_sorteio):
    nova_janela = ctk.CTkToplevel(janela_sorteio)
    nova_janela.title("Sorteio")
    nova_janela.geometry("400x300")
    ctk.CTkLabel(nova_janela, text="Página de Sorteio", font=("Arial", 18)).pack(pady=20)
# Funcoes das paginas

# Permite testar separadamente
if __name__ == '__main__':
    app = ctk.CTk()
    abrir_pagina_sorteio(app)
    app.mainloop()