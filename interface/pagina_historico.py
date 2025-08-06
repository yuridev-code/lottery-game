import os
import customtkinter as ctk

# pega o diretório raiz do projeto (uma pasta acima de interface)
Diretorio_RAIZ = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

# caminho absoluto para o arquivo historico.txt
Diretorio = os.path.join(Diretorio_RAIZ, 'dados', 'historico.txt')

def abrir_historico():
    janela = ctk.CTkToplevel()
    janela.title("Histórico de Sorteios")
    janela.geometry("500x400")
    # Cria uma caixa de texto:
    texto = ctk.CTkTextbox(janela, wrap='word')
    texto.pack(expand=True, fill="both", padx=10, pady=10)

    if os.path.exists(Diretorio):
        with open(Diretorio, 'r', encoding='utf-8') as arquivo:
            conteudo = arquivo.read()
            texto.insert("0.0", conteudo)
    else:
        texto.insert("0.0", "Nenhum histórico encontrado.")
