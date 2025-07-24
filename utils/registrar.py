import operacoes
def registrar_operacao(obter_numeros_usuario, sortear_numeros_loteria , verificar_acertos):
    obter_numero = obter_numeros_usuario()
    sortear_numeros = sortear_numeros_loteria()
    acertos = verificar_acertos()
    arquivo = open('registro.txt','a',encoding='utf-8')
    arquivo.write(f'Números escolhidos pelo usuário:\n {obter_numero}\n')
    arquivo.write(f'Números sorteados:\n {sortear_numeros}\n')
    arquivo.write(f'Acertos:\n {acertos}\n')
    arquivo.close()


