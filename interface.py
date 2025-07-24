import customtkinter as ctk
import tkinter as tk
from PIL import Image
import os

# Funcoes das paginas
def abrir_pagina_cadastro():
    nova_janela = ctk.CTkToplevel(app)
    nova_janela.title("Cadastro de Participantes")
    nova_janela.geometry("400x300")
    ctk.CTkLabel(nova_janela, text="Página de Cadastro", font=("Arial", 18)).pack(pady=20)


def abrir_pagina_sorteio():
    nova_janela = ctk.CTkToplevel(app)
    nova_janela.title("Sorteio")
    nova_janela.geometry("400x300")
    ctk.CTkLabel(nova_janela, text="Página de Sorteio", font=("Arial", 18)).pack(pady=20)

# Aparência
app = ctk.CTk()
app.title("Sorteio")
app.geometry("500x700")
ctk.set_default_color_theme("green")

# Topo
frame_topo = ctk.CTkFrame(app, fg_color="transparent")
frame_topo.pack(pady=20)



# LINHA DE SEPARAÇÃO
linha1 = ctk.CTkFrame(app, height=2, fg_color="#444444")
linha1.pack(fill="x", padx=40, pady=10)
# LINHA DE SEPARAÇÃO

# Caminho absoluto até a imagem
caminho_absoluto = os.path.join(os.path.dirname(__file__), "image", "trevo_4.jpg")
logo_img = ctk.CTkImage(Image.open(caminho_absoluto), size=(100, 100))
logo = ctk.CTkLabel(frame_topo, image=logo_img, text="")
logo.pack()
# imagem

# Titulo
Titulo = ctk.CTkLabel(frame_topo, text="Sorteadora Digital", font=("Helvetica", 28, "bold"))
Titulo.pack(pady=10)

# LINHA DE SEPARAÇÃO
linha2 = ctk.CTkFrame(app, height=2, fg_color="#444444")
linha2.pack(fill="x", padx=40, pady=20)
# LINHA DE SEPARAÇÃO

# BOTÕES 
frame_botoes = ctk.CTkFrame(app, fg_color="transparent")
frame_botoes.pack(pady=30)

botao_cadastro = ctk.CTkButton(frame_botoes, text="Ir para Cadastro", command=abrir_pagina_cadastro, width=200)
botao_cadastro.pack(pady=10)

botao_sorteio = ctk.CTkButton(frame_botoes, text="Ir para Sorteio", command=abrir_pagina_sorteio, width=200)
botao_sorteio.pack(pady=10)

# Iniciar a interface
app.mainloop()
