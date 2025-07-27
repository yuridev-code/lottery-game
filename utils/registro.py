from datetime import datetime

def registro(numeros_sorteados, numeros_adicionados, quantidade_de_acertos, numeros_acertados):
    with open("historico.txt", "w", encoding="utf-8") as arquivo:
        data_hora = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        arquivo.write(f"Ultima Aposta: {data_hora}\t")
        arquivo.write(f"Números Sorteados: {numeros_sorteados}\t")
        arquivo.write(f"Números Adicionados: {numeros_adicionados}\t")
        arquivo.write(f"Quantidade de Acertos: {quantidade_de_acertos}\t")
        arquivo.write(f"Acertos: {numeros_acertados}\t")
