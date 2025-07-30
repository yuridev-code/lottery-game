from datetime import datetime

def exibir(numeros_sorteados, numeros_adicionados, quantidade_de_acertos, numeros_acertados):
    data_hora = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    if numeros_sorteados == numeros_acertados:
        print('VOCÊ GANHOU MIZERAVI!!!\n')
        print(f"{data_hora}")
        print(f"Números Sorteados: {numeros_sorteados}")
        print(f"Números Adicionados: {numeros_adicionados}")
        print(f"Quantidade de Acertos: {quantidade_de_acertos}")
        print(f"Números Acertados: {numeros_acertados}")
    else:
        print('VOCÊ PERDEU MIZERAVI!!!\n')
        print(f"{data_hora}")
        print(f"Números Sorteados: {numeros_sorteados}")
        print(f"Números Adicionados: {numeros_adicionados}")
        print(f"Quantidade de Acertos: {quantidade_de_acertos}")
        print(f"Números Acertados: {numeros_acertados}")      
    return numeros_sorteados, numeros_adicionados, quantidade_de_acertos, numeros_acertados