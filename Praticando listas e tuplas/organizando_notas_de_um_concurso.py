"""
Uma escola realizou um concurso de redação, e o próximo passo é organizar as notas dos participantes para definir a ordem de premiação. Para garantir transparência, as notas precisam ser classificadas em ordem crescente, do menor para o maior valor.

Com base nisso, desenvolva um programa que receba como entrada uma lista contendo as notas de todos os participantes e exiba, ao final, essa lista ordenada em ordem crescente.

Exemplo de Entrada:

Notas: [85, 70, 90, 60, 75]

Saída esperada:

Notas ordenadas: [60, 70, 75, 85, 90]
"""
def ordena_lista(lista: list) -> list:
    """Função que recebe uma lista e retorna a mesma
    lista com os elementos ordenados do menor para o 
    maior.
    Paramêtro:
        lista (list): Uma lista.
    Retorno:
        lista (list): A mesma lista com os elementos 
        ordenados do menor para o maior.
    """
    try:
        if lista == []:
            raise ValueError
        else:
            lista.sort()
            return lista
    except ValueError:
        print("A lista não pode estar vazia.")
        
def apresenta_notas(lista: list) -> None:
    """Função que recebe uma lista de notas e 
    apresenta o índice e cada nota, linha a linha.
    Paramêtro:
        lista (list): A lista de notas.
    Retorno:
        None
    Print:
        Se houverem notas a serem exibidas, exibe o 
        índice e a nota respectivamente.
    """
    if lista is None:
        print("Não há notas para exibir")
    else:
        for indice, nota in enumerate(lista, start=1):
            print(f"{indice}: Nota {nota}")

if __name__ == "__main__":
    lista1 = [85, 70, 90, 60, 75]
    lista_ordenada = ordena_lista(lista1)
    apresenta_notas(lista_ordenada)
    lista_vazia = []
    lista_ordenada = ordena_lista(lista_vazia)
    apresenta_notas(lista_ordenada)