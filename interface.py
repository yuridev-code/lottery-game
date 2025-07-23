import customtkinter as ctk
import tkinter as tk
# Aparência
app = ctk.CTk()
app.title("Sorteio")
app.geometry("500x700")


campo_bemvindo = ctk.CTkLabel(app, text="Bem-vindo!!!")
campo_bemvindo.pack(pady=10)

# Iniciar a interface
app.mainloop()