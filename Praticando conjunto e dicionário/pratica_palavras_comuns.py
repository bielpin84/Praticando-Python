"""
Clara é editora de uma revista e deseja comparar dois artigos para identificar quais palavras aparecem em ambos. Sua tarefa é criar um programa que receba dois textos e exiba o conjunto de palavras comuns entre eles.

Exemplo de entrada:

Texto 1: O sol brilha forte no céu azul 

Texto 2: O céu azul anuncia um dia de sol intenso 

Saída esperada:

Palavras em comum: {'o', 'azul', 'sol', 'céu'} 
"""
def pega_texto(numero: int) -> str:
    while True:
        try:
            texto = input(f"Digite o texto {numero}: ").lower().strip()
            if not texto:
                raise ValueError
            else:
                return texto
        except ValueError:
            print("O texto não pode ser vazio.")

separa_palavras = lambda texto: set(texto.split())

compara_conjuntos = lambda a, b: a.intersection(b)

def apresenta_palavras(conjunto: set) -> None:
    print(f"Palavras em comum: {", ".join(conjunto)}")

if __name__ == "__main__":
    texto1 = pega_texto(1)
    texto2 = pega_texto(2)
    palavras1 = separa_palavras(texto1)
    palavras2 = separa_palavras(texto2)
    palavras_comuns = compara_conjuntos(palavras1, palavras2)
    apresenta_palavras(palavras_comuns)