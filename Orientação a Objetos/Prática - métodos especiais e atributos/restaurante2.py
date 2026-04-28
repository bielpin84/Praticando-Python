class Restaurante():
    def __init__(self, nome, categoria, ativo = False):
        self.nome = nome
        self.categoria = categoria
        self.ativo = ativo
        self.avaliacao = ""
        self.tipo_entrega = ""

if __name__ == "__main__":
    pizza_joy = Restaurante("Pizza Joy", "Pizzaria")
    print(f"""
Nome: {pizza_joy.nome}
Categoria: {pizza_joy.categoria}
Ativo: {pizza_joy.ativo}
Avaliação: {pizza_joy.avaliacao}
Tipo de Entrega: {pizza_joy.tipo_entrega}
""")