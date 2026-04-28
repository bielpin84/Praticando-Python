# Importando a biblioteca do CSV
import csv

# escrever um arquivo csv com a função open()
def escreve_csv(nome_arquivo, lista):
    # Abrir com newline='' evita linhas em branco no Windows
    with open(nome_arquivo, "w", newline='', encoding='utf-8') as f:
        escritor = csv.writer(f)
        # Se a lista contém sub-listas/tuplas, escrevemos várias linhas
        if lista and all(isinstance(row, (list, tuple)) for row in lista):
            escritor.writerows(lista)
        else:
            escritor.writerow(lista)

# ler um arquivo csv com a função open()
def ler_csv(caminho_arquivo):
    with open(caminho_arquivo, newline="") as f:
        leitor = csv.reader(f)
        for linha in leitor:
            print(linha)

if __name__ == "__main__":
    meu_arquivo = "./Leitura e Escrita de arquivos/dados.csv"
    minha_lista = [("nome","idade"),["Ana",32]]
    escreve_csv(meu_arquivo, minha_lista)
    ler_csv(meu_arquivo)