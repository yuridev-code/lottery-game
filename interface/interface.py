import customtkinter as ctk
from PIL import Image
import os

# importa as funções de outras páginas
from interface.pagina_sorteio import abrir_pagina_sorteio

def criar_janela_principal():
    # Aparência
    janela_inicial = ctk.CTk()
    janela_inicial.title("Sorteio")
    janela_inicial.geometry("500x700")
    ctk.set_default_color_theme("green")

    # Topo
    frame_topo = ctk.CTkFrame(janela_inicial, fg_color="transparent")
    frame_topo.pack(pady=20)

    # LINHA DE SEPARAÇÃO
    linha1 = ctk.CTkFrame(janela_inicial, height=2, fg_color="#444444")
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
        janela_inicial,
        text=texto_apresentacao,
        wraplength=400,
        justify="left",
        font=ctk.CTkFont(size=16)
    )
    label_apresentacao.pack(pady=20)



    # BOTÕES 
    frame_botoes = ctk.CTkFrame(janela_inicial, fg_color="transparent")
    frame_botoes.pack(pady=30)

    botao_sorteio = ctk.CTkButton(frame_botoes, text="Ir para Sorteio", command=lambda: abrir_pagina_sorteio(), width=200)
    botao_sorteio.pack(pady=10)

    # LINHA DE SEPARAÇÃO
    linha2 = ctk.CTkFrame(janela_inicial, height=2, fg_color="#444444")
    linha2.pack(fill="x", padx=40, pady=20)
    # LINHA DE SEPARAÇÃO

    # Iniciar a interface
    janela_inicial.mainloop()