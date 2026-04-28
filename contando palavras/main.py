from contador import contar_palavras

frase = input("Digite uma frase: ").strip()
if not frase:
    print("A frase não pode ser vazia.")
else:
    numero_de_palavras = contar_palavras(frase)
    if numero_de_palavras:
        print("Contagem de palavras:")
        for palavra, contagem in numero_de_palavras.items():
            print(f"'{palavra}': {contagem}")
    else:
        print("Nenhuma palavra encontrada na frase.")    