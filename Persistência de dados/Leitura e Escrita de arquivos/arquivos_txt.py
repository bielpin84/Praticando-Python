# escrever um arquivo de texto com a função open()
def escreve_texto(nome_arquivo, texto):
    with open(nome_arquivo, "w") as f:
        f.write(texto)

# ler um arquivo de texto com a função open()
def ler_texto(caminho_arquivo):
    with open(caminho_arquivo, "r") as f:
        conteudo = f.read()
    print(conteudo)

# escrever em um arquivo de texto com o modo append na função open()
def insere_texto(arquivo, texto):
    with open(arquivo, "a") as f:
        f.write(texto)

if __name__ == "__main__":
    meu_arquivo = "./Leitura e Escrita de arquivos/dados.txt"
    escreve_texto(meu_arquivo, "Olá mundo")
    ler_texto(meu_arquivo)
    insere_texto(meu_arquivo, "\nOutra coisa")
    ler_texto(meu_arquivo)