class Restaurante():
    nome = ""
    categoria = ""
    ativo = ""
    avaliacao = ""
    tipo_entrega = ""

if __name__ == "__main__":
    pizza_joy = Restaurante()
    pizza_joy.nome = "Pizza Joy"
    pizza_joy.categoria = "Pizzaria"
    pizza_joy.ativo = True
    pizza_joy.avaliacao = 5.0
    pizza_joy.tipo_entrega = "Parceira"
    print(f"""
Nome: {pizza_joy.nome}
Categoria: {pizza_joy.categoria}
Ativo: {pizza_joy.ativo}
Avaliação: {pizza_joy.avaliacao}
Tipo de Entrega: {pizza_joy.tipo_entrega}
""")
