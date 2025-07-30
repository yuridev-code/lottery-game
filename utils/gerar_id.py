import randomfr

def gerar_id():
    id_usuario = 0
    for i in range(7):
        id_usuario = (id_usuario*10)+(random.randint(0, 9))
    return id_usuario
       