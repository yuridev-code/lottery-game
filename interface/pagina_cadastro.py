import customtkinter as ctk

# Funcoes das paginas
import customtkinter as ctk

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

class CadastroApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Cadastro de Usuário")
        self.geometry("400x300")

        self.label_titulo = ctk.CTkLabel(self, text="Cadastro", font=("Arial", 20))
        self.label_titulo.pack(pady=20)

        self.entry_nome = ctk.CTkEntry(self, placeholder_text="Digite seu nome")
        self.entry_nome.pack(pady=10)

        self.entry_email = ctk.CTkEntry(self, placeholder_text="Digite seu e-mail")
        self.entry_email.pack(pady=10)

        self.botao_cadastrar = ctk.CTkButton(self, text="Cadastrar", command=self.cadastrar)
        self.botao_cadastrar.pack(pady=20)

        self.label_resultado = ctk.CTkLabel(self, text="")
        self.label_resultado.pack(pady=10)

    def cadastrar(self):
        nome = self.entry_nome.get()
        email = self.entry_email.get()
        if nome and email:
            # Aqui você pode chamar uma função para salvar no arquivo ou banco de dados
            self.label_resultado.configure(text=f"Usuário {nome} cadastrado com sucesso!")
        else:
            self.label_resultado.configure(text="Preencha todos os campos.")

def abrir_pagina_cadastro(janela_anterior=None):
    if janela_anterior:
        janela_anterior.withdraw()
    app = CadastroApp()
    app.mainloop()
    
# Permite testar separadamente
if __name__ == "__main__":
    app = CadastroApp()
    app.mainloop() 