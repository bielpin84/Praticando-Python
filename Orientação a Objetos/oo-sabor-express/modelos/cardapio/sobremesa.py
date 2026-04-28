from modelos.cardapio.item_cardapio import ItemCardapio

class Sobremesa(ItemCardapio):
    """Classe que representa uma sobremesa no cardápio."""
    def __init__(self, nome, preco, descricao):
        """Inicializa uma sobremesa com nome, preço e descrição.
            Parâmetros:
            nome (str): Nome da sobremesa.
            preco (float): Preço da sobremesa.
            descricao (str): Descrição da sobremesa.
            """
        super().__init__(nome, preco)
        self.descricao = descricao

    def __str__(self):
        """Retorna uma representação em string da sobremesa."""
        return f"{self.nome} - R$ {self.preco} - Descrição: {self.descricao}"
    
    def aplicar_desconto(self):
        """Aplica um desconto de 15% no preço da sobremesa."""
        self._preco -= (self._preco * 0.15)