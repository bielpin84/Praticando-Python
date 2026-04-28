"""
Usando construtor

class Carro():
    def __init__(self, modelo=None, cor=None, ano=None):
        self.modelo = modelo
        self.cor = cor
        self.ano = ano

if __name__ == "__main__":
    meu_carro = Carro("Fusca", "Vermelho", 1984)
    print(f"Modelo do meu carro: {meu_carro.modelo}")
    print(f"Cor do meu carro: {meu_carro.cor}")
    print(f"Ano do meu carro: {meu_carro.ano}")
"""
# Sem usar construtor:
class Carro():
    modelo = ""
    cor = ""
    ano = 0

if __name__ == "__main__":
    meu_carro = Carro()
    meu_carro.modelo = "Brasília"
    meu_carro.cor = "Amarela"
    meu_carro.ano = 1986
    print(f"Modelo do meu carro: {meu_carro.modelo}")
    print(f"Cor do meu carro: {meu_carro.cor}")
    print(f"Ano do meu carro: {meu_carro.ano}")