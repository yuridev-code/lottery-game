import operacoes
def registrar_operacao(obter_numeros_usuario, sortear_numeros_loteria , verificar_acertos):
    arquivo = open('registro.txt','a',encoding='utf-8')
    arquivo.write(f'Números escolhidos pelo usuário:\n {obter_numeros_usuario}\n')
    arquivo.write(f'Números sorteados:\n {sortear_numeros_loteria}\n')
    arquivo.write(f'Acertos:\n {verificar_acertos}\n')
    arquivo.close()
    return(arquivo)
