import customtkinter as ctk

# Funcoes das paginas
def abrir_pagina_cadastro(janela_cadastro):
    nova_janela = ctk.CTkToplevel(janela_cadastro)
    nova_janela.title("Cadastro de Participantes")
    nova_janela.geometry("400x300")
    ctk.CTkLabel(nova_janela, text="Página de Cadastro", font=("Arial", 18)).pack(pady=20)

# Permite testar separadamente
if __name__ == '__main__':
    app = ctk.CTk()
    abrir_pagina_cadastro(app)
    app.mainloop()