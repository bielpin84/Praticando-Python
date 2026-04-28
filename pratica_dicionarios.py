"""
1 - Crie um dicionário representando informações sobre uma pessoa, como nome, idade e cidade.
"""
pessoas = {
    "pessoa 1": {
        "nome": "Aurora",
        "idade": "1 mês",
        "cidade": "Rio de Janeiro"
    },
    "pessoa 2": {
        "nome": "Karina",
        "idade": "39 anos",
        "cidade": "Rio de Janeiro"
    },
    "pessoa 3": {
        "nome": "Gabriel",
        "idade": "41 anos",
        "cidade": "Rio de Janeiro"
    }
}
# print(pessoas)
"""
2 - Utilizando o dicionário criado no item 1:
Modifique o valor de um dos itens no dicionário (por exemplo, atualize a idade da pessoa);
Adicione um campo de profissão para essa pessoa;
Remova um item do dicionário.
"""
pessoas["pessoa 1"]["idade"] = "1 mês e 18 dias"
pessoas["pessoa 2"]["profissão"] = "Professora"
pessoas["pessoa 3"].pop("idade")
# print(pessoas)
"""
3 - Crie um dicionário que relacione os números de 1 a 5 aos seus respectivos quadrados.
"""
dic_dos_quadrados = {numero: numero*2 for numero in range(1, 6)}
# print(dic_dos_quadrados)
"""
4 - Crie um dicionário e verifique se uma chave específica existe dentro desse dicionário.
"""
def verifica_chave(chave):
    for pessoa in pessoas:
        print(pessoa)
        if chave in pessoas[pessoa]:
            print(f"{chave} de {pessoas[pessoa]['nome']} é {pessoas[pessoa][chave]}")
        else:
            print(f"{pessoas[pessoa]['nome']} não tem {chave}")

# verifica_chave("idade")
"""
5 - Escreva um código que conte a frequência de cada palavra em uma frase utilizando um dicionário.
"""
def conta_palavras_da_frase(frase: str) -> dict:
    frequencia_palavras = {}
    lista_de_palavras = frase.split(" ")
    for palavra in lista_de_palavras:
        frequencia_palavras[palavra] = frequencia_palavras.get(palavra, 0) + 1
    return frequencia_palavras

frase = "teste de teste de contagem de palavras teste"
# print(conta_palavras_da_frase(frase))
