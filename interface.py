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


# def exibir, def historico
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
caminho_da_imagem = os.path.join(os.path.dirname(__file__), "image", "trevo_4.jpg")
logo_img = ctk.CTkImage(Image.open(caminho_da_imagem), size=(100, 100))
logo = ctk.CTkLabel(frame_topo, image=logo_img, text="")
logo.pack()
# imagem

# Titulo
Titulo = ctk.CTkLabel(frame_topo, text="Sorteadora Digital", text_color="green", font=("Helvetica", 28, "bold"))
Titulo.pack(pady=10)


texto_apresentacao = (
    "🎉 Bem-vindo ao Sorteador da Sorte!\n\n"
    "Você está prestes a participar de uma experiência única e divertida! "
    "Escolha seus números, clique em sortear e veja se a sorte está do seu lado.\n\n"
    "💰 Quem sabe você não seria o próximo milionário, se esse sorteio fosse real?"
)

label_apresentacao = ctk.CTkLabel(
    app,
    text=texto_apresentacao,
    wraplength=400,
    justify="left",
    font=ctk.CTkFont(size=16)
)
label_apresentacao.pack(pady=20)



# BOTÕES 
frame_botoes = ctk.CTkFrame(app, fg_color="transparent")
frame_botoes.pack(pady=30)

botao_cadastro = ctk.CTkButton(frame_botoes, text="Ir para Cadastro", command=abrir_pagina_cadastro, width=200)
botao_cadastro.pack(pady=10)

botao_sorteio = ctk.CTkButton(frame_botoes, text="Ir para Sorteio", command=abrir_pagina_sorteio, width=200)
botao_sorteio.pack(pady=10)

# LINHA DE SEPARAÇÃO
linha2 = ctk.CTkFrame(app, height=2, fg_color="#444444")
linha2.pack(fill="x", padx=40, pady=20)
# LINHA DE SEPARAÇÃO


# Iniciar a interface
app.mainloop()
