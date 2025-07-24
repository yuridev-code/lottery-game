# Essa função adciona os dados a um arquivo.txt 
# Dados necessarios → Data, hora e lista do sorteio
from usuario_entrada import escolher_numeros_usuario
def historico():
        numero_do_usuario = escolher_numeros_usuario
        with open('historico.txt', 'a', encoding='utf-8') as arquivo:
                dados = arquivo.write(f'\n{numero_do_usuario}')
                return dados
historico()        