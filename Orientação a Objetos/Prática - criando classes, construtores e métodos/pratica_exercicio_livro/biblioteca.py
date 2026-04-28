"""
5. Crie um arquivo chamado biblioteca.py e importe a classe Livro neste arquivo.

6. No arquivo biblioteca.py, empreste o livro chamando o método emprestar e imprima se o livro está disponível ou não após o empréstimo.

7. No arquivo biblioteca.py, utilize o método estático verificar_disponibilidade para obter a lista de livros disponíveis publicados em um ano específico.
"""
from livro import Livro
# Criando livros
livro1 = Livro("1984", "George Orwell", 1949)
livro2 = Livro("O Senhor dos Anéis", "J.R.R. Tolkien", 1954)
# Apresentando livros
print(livro1)
print(livro2)
# Antes do empréstimo
print(f"'{livro1._titulo}' disponível? {'Sim' if livro1._disponivel else 'Não'}")
# Emprestando livro
livro1.emprestar()
# Após o empréstimo
print(f"'{livro1._titulo}' disponível? {'Sim' if livro1._disponivel else 'Não'}")
# Obtendo a lista de livros publicados em 1954
disponiveis_1954 = Livro.verificar_disponibilidade(1954)
# Apresentando a lista
print("Livros disponíveis publicados em 1954:")
for livro in disponiveis_1954:
    print(livro)
