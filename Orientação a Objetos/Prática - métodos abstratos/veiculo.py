"""
1. Crie uma classe chamada Veiculo com um método abstrato chamado ligar.
2. No mesmo arquivo, crie um construtor para a classe Veiculo que aceita os parâmetros marca e modelo.
"""
from abc import ABC, abstractmethod

class Veiculo(ABC):
    def __init__(self, marca, modelo):
        self._marca = marca
        self._modelo = modelo
        self._ligado = False
    
    @abstractmethod
    def ligar(self):
        if not self._ligado:
            self._ligado = True
            print("O veículo foi ligado")
        else:
            print("O veículo já está ligado.")
    
    @abstractmethod
    def desligar(self):
        if self._ligado:
            self._ligado = False
            print("O veículo foi desligado")
        else:
            print("O veículo já está desligado.")
    
    def __str__(self):
        return f"Marca: {self._marca}\nModelo: {self._modelo}\nEstado: {'ligado' if self._ligado else 'desligado'}"