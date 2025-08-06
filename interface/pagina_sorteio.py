import customtkinter as ctk
from utils.apostar_sortear import fazer_aposta_e_sortear
from utils.apostar_sortear import banca_doida
from interface.pagina_historico import abrir_historico


def abrir_pagina_sorteio():
    janela = ctk.CTk()
    janela.title("Sorteio Loteria")
    janela.geometry("500x500")

    ctk.set_appearance_mode("dark")

    label_info = ctk.CTkLabel(janela, text="Digite 6 números entre 1 e 60:", text_color="green", font=("Helvetica", 15, "bold"))
    label_info.pack(pady=(10, 2))

    # Novo frame para os resultados
    frame_resultado = ctk.CTkFrame(janela, fg_color="transparent")
    frame_resultado.pack(pady=1)

    # resultado e botão sortear
    labels_resultado = {
        "resultado": ctk.CTkLabel(janela, text="", text_color="yellow", font=("Helvetica", 18, "bold")),
        "id": ctk.CTkLabel(janela, text=""),
        "sorteio": ctk.CTkLabel(frame_resultado, text=""),
        "aposta": ctk.CTkLabel(frame_resultado, text=""),
        "acertos": ctk.CTkLabel(frame_resultado, text=""),
        "numeros_acertados": ctk.CTkLabel(frame_resultado, text="")
        }

    for label in labels_resultado.values():
        label.pack(pady=2)

    # Cria os campos de entrada e os posiciona em 2 linhas por 3 colunas
    # Cria um frame para conter os campos de entrada em grade
    frame_entradas = ctk.CTkFrame(janela, fg_color="transparent")
    frame_entradas.pack(pady=4)

    entrada_numeros_usuario = []
    numeros_entradas = 6
    colunas = 3
    for i in range(numeros_entradas):
        linha = i // colunas
        coluna = i % colunas

        entrada = ctk.CTkEntry(
            frame_entradas,
            width=50,
            justify='center'
        )
        # grid: posicionamento de widgets
        entrada.grid(row=linha, column=coluna, padx=10, pady=10)
        entrada_numeros_usuario.append(entrada)

    botao_sortear = ctk.CTkButton(janela, text="Sortear",fg_color="green", command=lambda: fazer_aposta_e_sortear(entrada_numeros_usuario, labels_resultado))
    botao_sortear.pack(pady=10)

    botao_historico = ctk.CTkButton(janela, text="Ver Histórico", fg_color="green", command=abrir_historico)
    botao_historico.pack(pady=10)
    
    botao_definido = ctk.CTkButton(janela, text="Banca Endoidou", fg_color="green", command=lambda:banca_doida(entrada_numeros_usuario, labels_resultado))
    botao_definido.pack(pady=10)

    janela.mainloop()
