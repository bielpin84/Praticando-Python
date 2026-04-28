"""
Ana é responsável pelo controle de estoque de uma loja de artigos para papelaria. Ela precisa de um programa que permita cadastrar produtos em forma de dados estruturados. O sistema deve solicitar o nome e a quantidade de três produtos e, ao final, exibir as informações cadastradas em um dicionário, onde cada produto será uma chave e a quantidade correspondente será o valor.

Exemplo de entrada:
Digite o nome do produto: Caneta 

Digite a quantidade: 50 

Digite o nome do produto: Caderno 

Digite a quantidade: 30 

Digite o nome do produto: Borracha 

Digite a quantidade: 20

Saída esperada:
Dicionário de produtos: {'Caneta': 50, 'Caderno': 30, 'Borracha': 20} 
"""
dicionario_de_produtos = {} 
for i in range(3):
    produto = input("Digite o nome do produto: ").strip().capitalize()
    dicionario_de_produtos[produto] = int(input("Digite a quantidade: "))

print(f"Dicionário de produtos: {dicionario_de_produtos}")



