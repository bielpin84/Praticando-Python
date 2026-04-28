"""
4. Identificando palavras mais longas em um texto
Sofia é revisora de textos e precisa identificar palavras muito longas em um parágrafo. Textos mais fáceis de ler costumam ter palavras curtas, então ela quer um programa que encontre palavras que tenham mais de 10 letras e as exiba em destaque.

Crie um programa que receba um texto e exiba todas as palavras que possuem mais de 10 letras. Caso nenhuma palavra longa seja encontrada, o programa deve avisar o usuário.

Exemplo de entrada:
Digite um texto: A programação estruturada facilitou o desenvolvimento de grandes sistemas computacionais
Saída esperada:
Palavras longas encontradas: programação, estruturada, desenvolvimento, computacionais 
Se nenhum palavra longa for encontrada:
Nenhuma palavra longa foi encontrada no texto.  
"""
def encontra_palavras_longas(texto: str) -> str:
    palavras_longas = ", ".join(palavra for palavra in texto.split() if len(palavra) > 10)
    if palavras_longas != "":
        return f"Palavras longas encontradas: {palavras_longas}"
    else:
        return "Nenhuma palavra longa foi encontrada no texto."

if __name__ == "__main__":
    teste = "A programação estruturada facilitou o desenvolvimento de grandes sistemas computacionais"
    print(encontra_palavras_longas(teste))
