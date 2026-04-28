"""
Camila adora receber amigos para jantares temáticos. Para o próximo encontro, ela quer garantir que a ordem de chegada seja respeitada, mas ainda precisa fazer ajustes na lista de convidados. Camila quer adicionar novos nomes e organizá-los em posições específicas.

Como você criaria um programa que mostre a lista inicial, permita a inserção de um novo nome em uma posição escolhida e exiba a lista atualizada?

Exemplo de Entrada:

Lista atual de convidados: ['Ana', 'Pedro', 'Carlos']
Digite o nome do novo convidado: João
Digite a posição na qual deseja inserir o convidado: 2

Saída esperada:

Lista atualizada de convidados: 
'Ana'
'João' 
'Pedro'
'Carlos'
"""
def atualiza_convidados(convidados: list) -> list:
    """
    Função que recebe uma lista de convidados, pede 
    um novo nome, uma posição e insere o nome na
    posição informados, devolvendo a lista 
    atualizada.
    Parâmetro:
        convidados (list): Lista original com os 
        nomes dos convidados.
    Inputs:
        nome (str): Novo nome a ser inserido.
        posicao (int): Posição que o nome será 
        inserido.
    Retorno:
        atualizada (list): Lista de convidados com o
        novo nome inserido na posição informados.
    """
    while True:
        novo_convidado = input("Digite o nome do novo convidado: ").strip().capitalize()
        if not novo_convidado:
            print("O nome do novo convidado não pode estar em branco.")
        elif novo_convidado.isdigit():
            print("O nome do convidado não pode ser um número.")
        else:
            try:
                posicao = int(input("Digite a posição na qual deseja inserir o convidado: "))
                if posicao < 1 or posicao > len(convidados) + 1:
                    raise ValueError
                else:
                    posicao -= 1
                    convidados.insert(posicao, novo_convidado)
                    return convidados
            except ValueError:
                print("Informe uma posição válida.")

def apresenta_convidados(convidados: list) -> None:
    """ 
    Função que apresenta ordenadamente os convidados
    de uma lista.
    Parâmetro:
        convidados (list): Uma lista contendo os 
        nomes dos convidados.
    Retorno:
        None
    Print:
        A lista ordenada dos convidados.
    """
    if convidados == []:
        print("Não há convidados na lista.")
    else:
        print("Lista de convidados:")
        for posicao, convidado in enumerate(convidados, start=1):
            print(f"{posicao}: {convidado}")

if __name__ == "__main__":
    convidados_originais = ['Ana', 'Pedro', 'Carlos']
    convidados_atualizados = atualiza_convidados(convidados_originais)
    apresenta_convidados(convidados_atualizados)

