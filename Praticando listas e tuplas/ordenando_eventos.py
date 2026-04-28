"""
A Futuro Eventos, uma empresa especializada em organização de conferências, cometeu um erro ao registrar a sequência dos eventos de uma conferência importante. Os eventos foram registrados na ordem inversa à que deveriam acontecer. Agora, a equipe precisa corrigir a ordem dos eventos para garantir que a conferência aconteça conforme o planejamento original.

Considerando a lista inicial de eventos, crie um programa que permita ao organizador ordená-los, de forma que a lista final siga a sequência correta.

eventos_registrados = ['Encerramento', 'Palestra 3', 'Palestra 2', 'Abertura']

Saída esperada:

Ordem corrigida: ['Abertura', 'Palestra 2', 'Palestra 3', 'Encerramento']
"""
def inverte_ordem(lista: list) -> list:
    """
    Função que recebe uma lista e retorna a mesma,
    porém com seus elementos em ordem invertida.
    Parâmetro:
        lista (list): Uma lista não vazia.
    Retorno:
        lista (list): A lista com os 
        elementos em ordem invertida.
    """
    lista.reverse()
    return lista

def apresenta_eventos(lista: list) -> None:
    """ 
    Função que apresenta ordenadamente os eventos na
    lista recebida.
    Parâmetro:
        lista (list): Uma lista contendo os eventos a
        serem apresentados.
    Retorno:
        None
    Print:
        A lista dos eventos em ordem.
    """
    if lista == []:
        print("Não há eventos inscritos.")
    else:
        print("Lista de eventos:")
        for indice, evento in enumerate(lista, start=1):
            print(f"{indice}: {evento}")

if __name__ == "__main__":
    eventos_registrados = ['Encerramento', 'Palestra 3', 'Palestra 2', 'Abertura']

    ordem_corrigida = inverte_ordem(eventos_registrados)

    apresenta_eventos(ordem_corrigida)