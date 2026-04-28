"""
1. Crie uma classe chamada Livro com um construtor que aceita os parâmetros titulo, autor e ano_publicacao. Inicie um atributo chamado disponivel como True por padrão.

2. Na classe Livro, adicione um método especial str que retorna uma mensagem formatada com o título, autor e ano de publicação do livro. Crie duas instâncias da classe Livro e imprima essas instâncias.

3. Adicione um método de instância chamado emprestar à classe Livro que define o atributo disponivel como False. Crie uma instância da classe, chame o método emprestar e imprima se o livro está disponível ou não.

4. Adicione um método estático chamado verificar_disponibilidade à classe Livro que recebe um ano como parâmetro e retorna uma lista dos livros disponíveis publicados nesse ano.
"""

class Livro:
    livros = []
    def __init__(self, titulo, autor, ano_publicacao):
        self._titulo = titulo
        self._autor = autor
        self._ano_publicacao = ano_publicacao
        self._disponivel = True
    
        Livro.livros.append(self)

    def __str__(self):
        return f"Livro: '{self._titulo}' por {self._autor} (Publicado em: {self._ano_publicacao})"
    
    def emprestar(self):
        if not self._disponivel:
            print(f"Erro no empréstimo, o livro {self._titulo} está indisponível.")
            return
        print(f"Livro {self._titulo} emprestado!")
        self._disponivel = False
    
    def devolver(self):
        if self._disponivel:
            print(f"Erro na entrega, o livro {self._titulo} já foi devolvido.")
            return
        print(f"Livro {self._titulo} devolvido!")
        self._disponivel = True
    
    @staticmethod
    def verificar_disponibilidade(ano):
        disponiveis_no_ano = [livro for livro in Livro.livros if livro._ano_publicacao == ano and livro._disponivel]
        return disponiveis_no_ano

if __name__ == "__main__":
    livro1 = Livro("1984", "George Orwell", 1949)
    livro2 = Livro("O Senhor dos Anéis", "J.R.R. Tolkien", 1954)

    print(livro1)
    print(livro2)
    livro1.emprestar()
    print(f"'{livro1._titulo}' disponível? {'Sim' if livro1._disponivel else 'Não'}")
    disponiveis_1954 = Livro.verificar_disponibilidade(1954)
    print("Livros disponíveis em 1954:")
    for livro in disponiveis_1954:
        print(livro)