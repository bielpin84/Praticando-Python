from abc import ABC, abstractmethod

class ItemCardapio(ABC):
    """Classe abstrata que representa um item do cardápio."""
    def __init__(self, nome, preco):
        """Inicializa um item do cardápio com nome e preço.
        Parâmetros:
        nome (str): Nome do item.
        preco (float): Preço do item.
        """
        self._nome = nome
        self._preco = preco

    @abstractmethod
    def aplicar_desconto(self):
        """Aplica um desconto ao preço do item."""
        pass