frase = "teste de teste de contagem de palavras teste"
def conta_palavras(frase):
    """Conta a ocorrência de cada palavra em uma frase.
    Args: frase (str): A frase a ser analisada.
    
    Returns: None
    Prints: um dicionário com a contagem de cada palavra.

    """
    contagem_palavras = {}
    palavras = frase.split()
    for palavra in palavras:
        contagem_palavras[palavra] = contagem_palavras.get(palavra, 0) + 1
    print(contagem_palavras)

conta_palavras(frase)
# Saída esperada: {'teste': 3, 'de': 2, 'contagem': 1, 'palavras': 1}

