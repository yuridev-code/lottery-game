from tkinter import messagebox
from utils.constantes import *

def validar_aposta(entry_numeros):
    """Valida e retorna a aposta do usuário como lista ordenada ou None se inválida."""

    aposta_usuario = set()
    for i, entry in enumerate(entry_numeros):
        try:
            numero = int(entry.get())
            if numero in aposta_usuario:
                messagebox.showwarning("Aposta Inválida", f"Número {numero} repetido.")
                return None
            if not (NUMERO_MINIMO_LOTERIA <= numero <= NUMERO_MAXIMO_LOTERIA):
                messagebox.showwarning("Aposta Inválida", f"Número {numero} fora do intervalo permitido.")
                return None
            aposta_usuario.add(numero)
        except ValueError:
            messagebox.showwarning("Erro", f"Campo {i+1} inválido. Digite um número.")
            return None

    if len(aposta_usuario) != QUANTIDADE_NUMEROS_LOTERIA:
        messagebox.showwarning("Erro", f"Digite exatamente {QUANTIDADE_NUMEROS_LOTERIA} números.")
        return None

    return sorted(list(aposta_usuario))