"""
5. Em um arquivo chamado main.py, importe a classe Carro.
6. No arquivo main.py, instancie três objetos da classe Carro com diferentes características, como marca, modelo e cor.
"""
from carro import Carro

carro1 = Carro("Honda", "Fit", "Prata")
print("Antes de ligar:")
print(carro1)
print("\nDepois de ligar: ")
carro1.ligar()
print(carro1)
print("\nTentando ligar novamente: ")
carro1.ligar()
carro2 = Carro("Fiat", "Uno", "Branco")
print("\nCarro 2:")
print(carro2)
carro3 = Carro("Toyota", "Corola", "Cinza")
print("\nCarro 3:")
print(carro3)
print("\nTentando desligar carro desligado: ")
carro3.desligar()