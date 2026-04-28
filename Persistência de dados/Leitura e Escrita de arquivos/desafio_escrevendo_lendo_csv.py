"""
Na Escola PythonVille, o professor quer registrar as notas dos alunos e depois consultar quem teve um bom desempenho.

Além disso, a coordenação precisa manter um registro organizado com essas informações para uso futuro.

O que você deve fazer:

Crie um programa que grave em um arquivo alunos.csv uma lista de alunos e suas notas.
Leia o arquivo alunos.csv e imprima apenas os alunos com nota maior ou igual a 7.0.
"""
import csv

def escreve_csv(nome_arquivo, lista):
    with open(nome_arquivo, "w", newline='', encoding='utf-8') as f:
        escritor = csv.writer(f)
        if lista and all(isinstance(row, (list, tuple)) for row in lista):
            escritor.writerows(lista)
        else:
            escritor.writerow(lista)

def ler_notas(caminho_arquivo, nota):
    with open(caminho_arquivo, newline="") as f:
        leitor = csv.reader(f)
        for linha in leitor:
            if float(linha[1]) >= nota:
                print(linha)

if __name__ == "__main__":
    documento = "./Leitura e Escrita de arquivos/alunos.csv"
    lista_alunos = [
        ["Roberto", 5.5],
        ["Ana", 9.0],
        ["Clara", 7.5],
        ["David", 7.0],
        ["João", 10.0],
        ["Thiago", 6.5],
        ["Luiz", 8.0],
        ["Francisco", 4.4],
        ["Leandro", 6.0]
    ]
    escreve_csv(documento, lista_alunos)
    ler_notas(documento, 7.0)