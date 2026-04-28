# Importando a biblioteca JSON
import json

# escrever um arquivo json com a função open()
def escrever_json(arquivo, dados):
    with open(arquivo, "w") as f:
        json.dump(dados, f)

# ler um arquivo json com a função open()
def ler_json(arquivo):
    with open(arquivo, "r") as f:
        dados_lidos = json.load(f)
        print(dados_lidos)

if __name__ == "__main__":
    meu_arquivo = "./Leitura e Escrita de arquivos/dados.json"
    meu_dict = {
        "Nome": "Ana",
        "Idade": 32,
        "Endereços": ["a", "b"]
    }
    escrever_json(meu_arquivo, meu_dict)
    ler_json(meu_arquivo)