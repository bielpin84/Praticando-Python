from modelos.avaliacao import Avaliacao
from modelos.cardapio.item_cardapio import ItemCardapio

class Restaurante:
    """Representa um restaurante no sistema Sabor Express."""

    restaurantes = []

    def __init__(self, nome, categoria):
        """Inicializa uma instância de um novo restaurante.
        Parâmetros:
        nome (str): Nome do restaurante.
        categoria (str): Categoria do restaurante (e.g., "Italiana", "Chinesa").
        """
        self._nome = nome.title()
        self._categoria = categoria.upper()
        self._ativo = False
        self._avaliacoes = []
        self._cardapio = []
        Restaurante.restaurantes.append(self)
    
    def __srt__(self):
        """Retorna uma representação em string do restaurante."""
        return f"Restaurante: {self._nome} - Categoria: {self._categoria}"
    
    @classmethod
    def listar_restaurantes(cls):
        """Lista todos os restaurantes cadastrados."""
        print(f"{'Nome do Restaurante'.ljust(25)} | {'Categoria'.ljust(25)} | {'Avaliação'.ljust(25)} | {'Status'}")
        for restaurante in cls.restaurantes:
            print(f"{restaurante._nome.ljust(25)} | {restaurante._categoria.ljust(25)} | {str(restaurante.media_avaliacoes).ljust(25)} | {restaurante.ativo}")
    
    @property
    def ativo(self):
        """Retorna o status visual do restaurante."""
        return "☑" if self._ativo else "☐" # Símbolos visuais retirados de https://coolsymbol.com/

    def alternar_estado(self):
        """Alterna o estado do restaurante entre ativo e inativo."""
        self._ativo = not self._ativo

    def receber_avaliacao(self, cliente, nota):
        """Adiciona uma nova avaliação ao restaurante.
        Parâmetros:
        cliente (str): Nome do cliente que fez a avaliação.
        nota (int): Nota dada pelo cliente (de 1 a 5).
        """
        if 0 < nota <= 5:
            avaliacao = Avaliacao(cliente, nota)
            self._avaliacoes.append(avaliacao)

    @property
    def media_avaliacoes(self):
        """Calcula e retorna a média das avaliações do restaurante."""
        if not self._avaliacoes:
            return "-"
        soma_das_notas = sum(avaliacao._nota for avaliacao in self._avaliacoes)
        quantidade_de_notas = len(self._avaliacoes)
        media = round(soma_das_notas / quantidade_de_notas, 1)
        return media

    def adicionar_no_cardapio(self, item):
        """Adiciona um item ao cardápio do restaurante.
        Parâmetros:
        item (ItemCardapio): Instância de ItemCardapio a ser adicionada.
        """
        if isinstance(item, ItemCardapio):
            self._cardapio.append(item)

    @property
    def exibir_cardapio(self):
        """Exibe o cardápio do restaurante."""
        print(f"Cardápio do Restaurante {self._nome}\n")
        for i, item in enumerate(self._cardapio, start=1):
            if hasattr(item, 'descricao'):
                mensagem_prato = f"{i}. Nome: {item._nome} | Preço: R$ {item._preco} | Descrição: {item.descricao}"
                print(mensagem_prato)
            else:
                mensagem_bebida = f"{i}. Nome: {item._nome} | Preço: R$ {item._preco} | Tamanho: {item.tamanho}"
                print(mensagem_bebida)


if __name__ == "__main__":
    r1 = Restaurante("SABOR ITALIANO", "italiana")
    r2 = Restaurante("delícias da china", "Chinesa")
    r3 = Restaurante("TaCo LoCo", "MexiCana")

    r1.alternar_estado()
    r3.alternar_estado()

    Restaurante.listar_restaurantes()