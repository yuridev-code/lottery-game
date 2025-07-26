
from datetime import datetime

def historico(numeros_sorteados, numeros_adicionados, quantidade_de_acertos, numeros_acertados):
    with open("historico.txt", "a", encoding="utf-8") as arquivo:
        arquivo.write("-=" * 40 + "\n")
        data_hora = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        arquivo.write(f"Data e Hora: {data_hora}\n")
        arquivo.write(f"Números Sorteados: {numeros_sorteados}\n")
        arquivo.write(f"Números Adicionados: {numeros_adicionados}\n")
        arquivo.write(f"Quantidade de Acertos: {quantidade_de_acertos}\n")
        arquivo.write(f"Acertos: {numeros_acertados}\n")
