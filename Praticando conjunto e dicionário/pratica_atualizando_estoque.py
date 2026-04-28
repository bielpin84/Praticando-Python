"""
Ana percebeu que, após o cadastro inicial dos produtos, precisa atualizar a quantidade de um item específico no estoque. Sua tarefa é criar um programa que solicite o nome do produto e a nova quantidade, atualizando essa informação no dicionário de estoque.

Exemplo de entrada:

estoque = { 

    "Caderno universitário": 50, 

    "Caneta azul": 120, 

    "Borracha branca": 30 

} 
Nome do produto a ser atualizado: Caneta azul 

Nova quantidade: 150 

Saída esperada:

{ 

    "Caderno universitário": 50, 

    "Caneta azul": 150, 

    "Borracha branca": 30 

} 
"""
estoque = {
    "Caderno universitário": 50,
    "Caneta azul": 120,
    "Borracha branca": 30
    }
produto = input("Nome do produto a ser atualizado: ").strip().capitalize()
if produto in estoque:
    quantidade = int(input("Nova quantidade: "))
    estoque[produto] = quantidade
    print(estoque)
else:
    print("Produto não encontrado.")