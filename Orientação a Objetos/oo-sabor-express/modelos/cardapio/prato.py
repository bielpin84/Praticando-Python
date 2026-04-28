from modelos.cardapio.item_cardapio import ItemCardapio

class Prato(ItemCardapio):
    """Classe que representa um prato no cardápio."""
    def __init__(self, nome, preco, descricao):
        """Inicializa um prato com nome, preço e descrição.
            Parâmetros:
            nome (str): Nome do prato.
            preco (float): Preço do prato.
            descricao (str): Descrição do prato.
            """
        super().__init__(nome, preco)
        self.descricao = descricao
    
    def __str__(self):
        """Retorna uma representação em string do prato."""
        return f"{self.nome} - R$ {self.preco} - Descrição: {self.descricao}"
    
    def aplicar_desconto(self):
        """Aplica um desconto de 80% no preço do prato."""
        self._preco -= (self._preco * 0.8)