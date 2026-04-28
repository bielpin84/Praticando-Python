class Restaurante():
    def __init__(self, nome, categoria, ativo = False):
        self.nome = nome
        self.categoria = categoria
        self.ativo = ativo
    
    def __str__(self):
        return f"Restaurante {self.nome}, categoria {self.categoria}"

if __name__ == "__main__":
    restaurante_arabe = Restaurante("Kibezarro", "Árabe")
    print(restaurante_arabe)