"""
3. Crie uma nova classe chamada Carro que herda da classe Veiculo.
4. No construtor da classe Carro, utilize o método super() para chamar o construtor da classe pai e atribua o atributo específico cor à classe filha.
"""
from veiculo import Veiculo

class Carro(Veiculo):
    def __init__(self, marca, modelo, cor):
        super().__init__(marca, modelo)
        self._cor = cor
    
    def ligar(self):
        if not self._ligado:
            self._ligado = True
            print("O carro foi ligado.")
        else:
            print("O carro já está ligado.")
    
    def desligar(self):
        if self._ligado:
            self._ligado = False
            print("O carro foi desligado")
        else:
            print("O carro já está desligado.")
    
    def __str__(self):
        return f"{super().__str__()}\nCor: {self._cor}"