"""
O clube de atletismo Alura Runners organizou uma corrida e divulgou a lista com a classificação final dos participantes. Mas, um erro foi identificado: um dos nomes está incorreto. O organizador precisa de um programa que permita localizar o nome errado e substituí-lo pelo correto.

Como você escreveria um programa que solicite o nome errado, o nome correto e atualize a lista exibindo a nova classificação ao final?

Exemplo de Entrada:

Digite o nome incorreto: Carlos
Digite o nome correto: João

Saída esperada:

O nome Carlos foi substituído por João.
Lista atualizada: ['Ana', 'João', 'Pedro']
"""
def troca_nome(lista: list) -> list:
    nome_incorreto = input("Digite o nome incorreto: ").strip().capitalize()
    if nome_incorreto in lista:
        while True:
            nome_correto = input("Digite o nome correto: ").strip().capitalize()
            if not nome_correto or nome_correto.isdigit():
                print("Você deve inserir um nome válido.")
            else:
                posicao = lista.index(nome_incorreto)
                lista.remove(nome_incorreto)
                lista.insert(posicao, nome_correto)
                return lista
    else:
        print("Nome não encontrado.")
        return lista

def mostra_iteravel_em_ordem(iteravel) -> None:
    for indice, item in enumerate(iteravel, start=1):
        print(f"{indice}: {item}")

if __name__ == "__main__":
    classificacao = ["Ana", "Carlos", "Pedro"]
    classificacao_correta = troca_nome(classificacao)
    print("Classificação correta:")
    mostra_iteravel_em_ordem(classificacao_correta)
