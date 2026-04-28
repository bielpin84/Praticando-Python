"""
3. Contagem de vogais em um texto
Mariana é professora de língua portuguesa e quer um programa que conte quantas vogais há em um texto digitado pelos alunos. Isso ajudará a analisar a estrutura das palavras utilizadas.

Crie um programa que peça um texto e exiba quantas vogais (a, e, i, o, u) ele contém.

Exemplo de entrada:
Digite um texto: A linguagem Python é muito versátil.
Saída esperada:
O texto contém 13 vogais.
"""

import unicodedata as ucd

def normalizando(texto: str) -> str:
    return "".join(c for c in ucd.normalize("NFD", texto) if ucd.category(c) != "Mn")

def contar_vogais(texto: str) -> int:
    return sum(1 for letra in normalizando(texto).lower() if letra in "aeiou")

if __name__ == "__main__":
    teste = "A linguagem Python é muito versátil"
    print(f"Texto a ser analizado:\n'{teste}'\n")
    print(f"O texto contém {contar_vogais(teste)} vogais.")