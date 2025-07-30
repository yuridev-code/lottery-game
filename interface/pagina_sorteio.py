import customtkinter as ctk
from utils.apostar_sortear import fazer_aposta_e_sortear
from utils.apostar_sortear import banca_doida
from interface.pagina_historico import abrir_historico


def abrir_pagina_sorteio():
    janela = ctk.CTk()
    janela.title("Sorteio Loteria")
    janela.geometry("500x500")

    ctk.set_appearance_mode("dark")
    ctk.set_default_color_theme("blue")

    label_info = ctk.CTkLabel(janela, text="Digite 6 números entre 1 e 60:", text_color="green", font=("Helvetica", 15, "bold"))
    label_info.pack(pady=(10, 2))

    # Novo frame para os resultados
    frame_resultado = ctk.CTkFrame(janela, fg_color="transparent")
    frame_resultado.pack(pady=1)


    # resultado e botão sortear
    labels_resultado = {
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

    entry_numeros = []
    for i in range(6):
        entry = ctk.CTkEntry(frame_entradas, width=50, justify='center')
        entry.grid(row=i // 3, column=i % 3, padx=10, pady=10)
        entry_numeros.append(entry)

    for label in labels_resultado.values():
        label.pack(pady=2)

    botao_sortear = ctk.CTkButton(janela, text="Sortear", command=lambda: fazer_aposta_e_sortear(entry_numeros, labels_resultado))
    botao_sortear.pack(pady=10)

    botao_historico = ctk.CTkButton(janela, text="Ver Histórico", command=abrir_historico)
    botao_historico.pack(pady=10)
    
    botao_definido = ctk.CTkButton(janela, text="Banca endoidou", command=lambda:banca_doida)
    botao_definido.pack(pady=10)

    janela.mainloop()
