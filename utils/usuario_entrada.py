import random

def escolher_numeros_usuario():

    numero_usuario = set()
    print("Escolha 6 númeors para sua aposta entre 1 e 60. ")
    while len(numero_usuario) < 6:
        try:
            numero= int(input(f"Escolha o {len(numero_usuario) +1}º número: "))
            if numero < 1 or numero > 60:
                print("Escolha um número válido entre 1 e 60: ")
            elif numero in numero_usuario:
                print("Você ja escolheu esse numero, digite outro número.")
            else:
                numero_usuario.add(numero)
        except ValueError:
            print("Entrada inválida. Digite um número inteiro.")
    return sorted(list(numero_usuario))

