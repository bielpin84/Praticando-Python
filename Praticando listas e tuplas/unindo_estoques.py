"""
Armano trabalha com a gestão de dois estoques de mercadorias que são representados como tuplas. Agora, ele precisa criar um relatório unificado com os produtos dos dois estoques juntos.

Para ajudá-lo, como você criaria um programa que ler as informações dos estoques e gera um relatório com todos os produtos juntos?

Exemplo de Entrada:

Produtos do estoque 1 (separados por vírgula): Arroz, Feijão, Macarrão
Produtos do estoque 2 (separados por vírgula): Óleo, Sal, Açúcar

Saída esperada:

Estoque combinado:
('Arroz', 'Feijão', 'Macarrão', 'Óleo', 'Sal', 'Açúcar')

estoque1 = tuple(input("Produtos do estoque 1 (separados por vírgula): ").split(", "))

estoque2 = tuple(input("Produtos do estoque 2 (separados por vírgula): ").split(", "))

estoque_combinado = estoque1 + estoque2
print(estoque_combinado)
"""
def forma_estoque(numero: int) -> tuple:
    """
    Função que pede ao usuário os produtos que estão
    no estoque e devolve uma tupla com os produtos.
    Parâmetro: 
        numero (int): Número identificador do
        estoque.
    Input:
        entrada (str): Produtos que estão no estoque.
    Retorno:
        estoque (tuple): Tupla formada pelos produtos
        informados na entrada após serem separados.
    """
    while True:
        entrada = input(f"Produtos do estoque {numero} (separados por vírgula): ").strip()
        
        if not entrada:
            print("O estoque informado não pode estar vazio.")
        else:
            estoque = tuple(item.strip().capitalize() for item in entrada.split(","))
            
            return estoque

def combina_estoques(estoque_a: tuple, estoque_b: tuple) -> tuple:
    """ 
    Função que recebe dois estoques em tuplas e as
    concatena em uma única tupla, certificando que
    os produtos não são repetidos.
    Parâmetro:
        estoque_a (tuple): Uma tupla contendo os
        produtos contidos em um estoque.
        estoque_b (tuple): Uma tupla contendo os
        produtos contidos em outro estoque.
    Retorno:
        Uma tupla contendo os produtos dos estoques 
        combinados.
    """
    return tuple(set(estoque_a + estoque_b))

def apresenta_estoque(estoque: tuple) -> None:
    """ 
    Função que apresenta ordenadamente os produtos
    contidos em um estoque.
    Parâmetro:
        estoque (tuple): Uma tupla contendo os produtos do estoque.
    Retorno:
        None
    Print:
        Os produtos do estoque enumerados.
    """
    if estoque == ():
        print("Não há produtos no estoque.")
    else:
        print("Lista de produtos no estoque:")
        for indice, produto in enumerate(estoque, start=1):
            print(f"{indice}: {produto}")

if __name__ == "__main__":
    estoque1 = forma_estoque(1)
    estoque2 = forma_estoque(2)
    
    estoque_combinado = combina_estoques(estoque1, estoque2)
    
    apresenta_estoque(estoque_combinado)

