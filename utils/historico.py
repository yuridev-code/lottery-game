def historico(sorteio, aposta, acertos, numeros_acertados):
    with open("dados/historico.txt", 'a', encoding="utf-8") as f:
        texto_acertados =", ".join(map(str, numeros_acertados))
        if acertos == 0:
            texto_acertados = "Nenhum" 
        else:
            ", ".join(map(str, numeros_acertados))
        
        f.write(
            f"Sorteio: {sorteio} | Aposta: {aposta} | Acertos: {acertos} | Números Acertados: {texto_acertados}\n"
        )
