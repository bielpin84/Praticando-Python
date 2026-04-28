"""Lucas é voluntário na organização de uma maratona e recebeu a lista de participantes com suas respectivas idades. Agora, ele precisa de um programa que apresente três informações:

Os nomes de todos os participantes.

As idades de todos os participantes.

Uma relação completa com o nome e a idade de cada um.

Sua tarefa é criar esse programa com base nas informações fornecidas.

Exemplo de entrada:

participantes = { 

    "Mariana": 25, 

    "Carlos": 32, 

    "Beatriz": 28, 

    "Rafael": 35 

} 

Saída esperada:


Nomes dos participantes: Mariana, Carlos, Beatriz, Rafael 

Idades dos participantes: 25, 32, 28, 35 

Participantes e suas idades: 

- Mariana: 25 anos 

- Carlos: 32 anos 

- Beatriz: 28 anos 

- Rafael: 35 anos 
"""
participantes = {
    "Mariana": 25,
    "Carlos": 32,
    "Beatriz": 28,
    "Rafael": 35
    }

print(f"Nomes dos participantes: {', '.join(participantes.keys())}")
print(f"Idades dos participantes: {', '.join(str(idade) for idade in participantes.values())}")
print("Participantes e suas idades:")
for nome, idade in participantes.items():
    print(f"{nome}: {idade} anos")