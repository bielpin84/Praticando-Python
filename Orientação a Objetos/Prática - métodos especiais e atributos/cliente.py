class Cliente():
    def __init__(self, nome, genero, idade, avaliacao):
        self. nome = nome
        self.genero = genero
        self.idade = idade
        self.avaliacao = avaliacao
    
    def __str__(self):
        return f"Nome do cliente: {self.nome}"
    
if __name__ == "__main__":
    cliente1 = Cliente("João", "masculino", 7, 4.0)
    cliente2 = Cliente("Maria", "feminino", 9, 4.5)
    cliente3 = Cliente("Bruxa", "feminino", 89, 0.0)
    print(cliente1)
    print(cliente2)
    print(cliente3)