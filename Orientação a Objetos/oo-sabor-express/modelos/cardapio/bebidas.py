from modelos.cardapio.item_cardapio import ItemCardapio

class Bebida(ItemCardapio):
    """Classe que representa uma bebida no cardápio."""
    def __init__(self, nome, preco, tamanho):
        """Inicializa um prato com nome, preço e descrição.
            Parâmetros:
            nome (str): Nome da bebida.
            preco (float): Preço da bebida.
            tamanho (str): Tamanho da bebida.
            """
        super().__init__(nome, preco)
        self.tamanho = tamanho

    def __str__(self):
        """Retorna uma representação em string da bebida."""
        return f"{self.nome} - R$ {self.preco} - Tamanho: {self.tamanho}"
    
    def aplicar_desconto(self):
        """Aplica um desconto de 50% no preço da bebida."""
        self._preco -= (self._preco * 0.5)