import string
import re

def limpar_texto_com_string(texto):
    """
    Remove pontuações e caracteres especiais de uma string de texto.

    Parâmetros:
    texto (str): A string de texto a ser limpa.

    Retorna:
    str: A string limpa, sem pontuações ou caracteres especiais.
    """
    tabela_traducao = str.maketrans('', '', string.punctuation)
    texto_limpo = texto.translate(tabela_traducao)
    return texto_limpo.lower()

def limpar_texto_manual(texto):
    """
    Remove pontuações e caracteres especiais de uma string de texto manualmente.

    Parâmetros:
    texto (str): A string de texto a ser limpa.

    Retorna:
    str: A string limpa, sem pontuações ou caracteres especiais.
    """
    caracteres_especiais = '''!()-[]{};:'"\\,<>./?@#$%^&*_~'''
    texto_limpo = ''
    for char in texto:
        if char not in caracteres_especiais:
            texto_limpo += char
    return texto_limpo.lower()


def limpar_texto_regex(texto):
    """
    Remove pontuações e caracteres especiais de uma string de texto usando expressões regulares.

    Parâmetros:
    texto (str): A string de texto a ser limpa.

    Retorna:
    str: A string limpa, sem pontuações ou caracteres especiais.
    """
    texto_limpo = re.sub(r'[^\w\s]', '', texto)
    return texto_limpo.lower()

def limpar_texto(texto):
    """
    Remove pontuações e caracteres especiais de uma string de texto.

    Parâmetros:
    texto (str): A string de texto a ser limpa.

    Retorna:
    str: A string limpa, sem pontuações ou caracteres especiais.
    """
    texto = texto.lower()
    caracteres = ",.!|?;:\"'()[]{}"
    for char in caracteres:
        texto = texto.replace(char, "")
    return texto

def contar_palavras(texto):
    """
    Conta a ocorrência de cada palavra em uma string de texto.

    Parâmetros:
    texto (str): A string de texto a ser analisada.

    Retorna:
    dict: Um dicionário com as palavras como chaves e suas contagens como valores.
    """
    texto = limpar_texto(texto)
    if not texto.strip():
        return {}
    palavras = texto.split()
    contagem = {}
    for palavra in palavras:
        contagem[palavra] = contagem.get(palavra, 0) + 1
    return contagem

# Testes das funções
if __name__ == "__main__":
    frases_teste = [
        "Olá, mundo! Este é um teste.",
        "Python é incrível: fácil de aprender, poderoso e versátil.",
        "Contar palavras é divertido; vamos contar juntos?",
        "Python PYTHON python!!!"
    ]
    for frase in frases_teste:
        print(f"Frase original: {frase}")
        print(f"Limpeza com string.punctuation: {limpar_texto_com_string(frase)}")
        print(f"Limpeza manual: {limpar_texto_manual(frase)}")
        print(f"Limpeza com regex: {limpar_texto_regex(frase)}")
        print(f"Limpeza simples: {limpar_texto(frase)}")
        print(f"Contagem de palavras: {contar_palavras(frase)}")
        print("-" * 40)
