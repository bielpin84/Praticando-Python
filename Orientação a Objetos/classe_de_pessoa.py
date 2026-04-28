class Pessoa:
    def __init__(self, nome, idade, profissao):
        """Inicializa uma nova pessoa.
        Parâmetros:
        nome (str): Nome da pessoa.
        idade (int): Idade da pessoa.
        profissao (str): Profissão da pessoa.
        """
        self.nome = nome
        self.idade = idade
        self.profissao = profissao

    def __str__(self):
        """Retorna uma representação em string da pessoa."""
        return f"Nome: {self.nome}, Idade: {self.idade}, Profissão: {self.profissao}"
    
    def aniversario(self):
        """Incrementa a idade da pessoa em 1 ano."""
        self.idade += 1

    @property
    def saudacao(self):
        """Retorna uma saudação personalizada."""
        if self.profissao:
            return f"Olá, meu nome é {self.nome}, tenho {self.idade} anos e trabalho como {self.profissao}."
        else:
            return f"Olá, meu nome é {self.nome} e tenho {self.idade} anos."

if __name__ == "__main__":
    p1 = Pessoa("Ana", 28, "Engenheira")
    p2 = Pessoa("Bruno", 34, "Médico")
    p3 = Pessoa("Carla", 22, "")

    print(p1)
    print(p2.saudacao)
    print(p3.saudacao)

    p1.aniversario()
    print(f"Após o aniversário, {p1.nome} agora tem {p1.idade} anos.")