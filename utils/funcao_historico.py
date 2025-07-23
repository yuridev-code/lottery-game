from operacoes import exibir_resultados
with open('historico.txt', 'a', encoding='utf-8') as arquivo:
        arquivo.write(f"\nNúmeros sorteados: {sorted(numeros_sorteados)}, Seus números: {sorted(numeros_usuario)}, Você acertou {len(numeros_acertados)} número(s): {sorted(numeros_acertados)}" )
