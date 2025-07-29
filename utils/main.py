# from interface.interface import criar_janela_principal

# if __name__ == "__main__":
#     criar_janela_principal()

from interface.pagina_sorteio import SorteioApp

if __name__ == '__main__':
    app = SorteioApp()
    app.mainloop()