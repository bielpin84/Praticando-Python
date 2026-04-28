"""
7. Crie um Arquivo Main (main.py): Crie um arquivo chamado main.py no mesmo diretório que suas classes.
8. Importe e Instancie Objetos: No arquivo main.py, importe as classes Carro e Moto. Em seguida, crie três instâncias de Carro e Moto com diferentes marcas, modelos, quantidade de portas e tipos.
9. Exiba as Informações: Para cada instância, imprima no console as informações utilizando o método str.
"""
from carro import Carro
from moto import Moto

carro1 = Carro("Fiat", "Uno", 2)
carro2 = Carro("Honda", "Civic", 4)
carro3 = Carro("Ford", "Ka", 4)
moto1 = Moto("Honda", "Bis", "Casual")
moto2 = Moto("Suzuki", "S450", "Esportiva")
moto3 = Moto("Yamaha", "Fast", "Esportiva")

print(carro1)
print(carro2)
print(carro3)
print(moto1)
print(moto2)
print(moto3)