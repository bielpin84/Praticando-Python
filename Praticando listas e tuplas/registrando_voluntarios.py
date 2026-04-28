"""
Uma ONG está organizando uma campanha de arrecadação de alimentos e precisa registrar os nomes dos voluntários que vão ajudar na ação. À medida que os voluntários se inscrevem, seus nomes devem ser adicionados à lista e quando for digitado a palavra sair o programa deve encerrar.

Ajude a ONG a criar um programa que permita registrar os voluntários e exiba a lista completa no final.

Exemplo de Entrada:

Digite o nome do voluntário (ou 'sair' para encerrar): Ana
Digite o nome do voluntário (ou 'sair' para encerrar): João
Digite o nome do voluntário (ou 'sair' para encerrar): Mariana
Digite o nome do voluntário (ou 'sair' para encerrar): sair

Saída esperada:
Voluntários registrados: ['Ana', 'João', 'Mariana']
"""
def forma_lista() -> list:
    """ 
    Função que pede ao usuário para inserir 
    nomes, e os adiciona a uma lista.
    Parâmetro: 
        None
    Input:
        Recebe nomes de voluntários.
    Retorno:
        voluntarios (list): Lista de voluntários
    """
    voluntarios = []
    while True:
        voluntario = input("Digite o nome do voluntário (ou 'sair' para encerrar)").strip().lower()
        if voluntario == "sair":
            return voluntarios
        elif not voluntario:
            print("O nome não pode estar em branco.")
        else:
            voluntarios.append(voluntario.capitalize())

def apresenta_voluntarios(lista: list) -> None:
    """ 
    Função que apresenta ordenadamente os voluntários
    inscritos na lista recebida.
    Parâmetro:
        lista (list): Uma lista contendo os nomes a
        serem apresentados.
    Retorno:
        None
    Print:
        A lista dos voluntários.
    """
    if lista == []:
        print("Não há voluntários inscritos.")
    else:
        print("Lista de voluntários inscritos:")
        for indice, nome in enumerate(lista, start=1):
            print(f"{indice}: {nome}")

if __name__ == "__main__":
    lista_de_voluntarios = forma_lista()
    apresenta_voluntarios(lista_de_voluntarios)

