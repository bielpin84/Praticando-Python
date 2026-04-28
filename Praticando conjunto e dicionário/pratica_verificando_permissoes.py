"""
Marina trabalha no setor de segurança de uma empresa e precisa verificar se um determinado conjunto de permissões faz parte das permissões principais de um sistema. Sua tarefa é desenvolver um programa que receba duas listas de permissões e verifique se a segunda lista está contida na primeira.

Exemplo de entrada:

> CASO 01: 

Permissões principais: leitura, escrita, execução, compartilhamento 

Permissões solicitadas: leitura, escrita 

> CASO 02: 

Permissões principais: leitura, escrita, execução, compartilhamento 

Permissões solicitadas: leitura, exclusão 

Saída esperada:

> CASO 01: 

As permissões solicitadas fazem parte das permissões principais. 

> CASO 02: 

As permissões solicitadas não fazem parte das permissões principais. 
"""
def forma_lista(tipo: str) -> set:
    while True:
        lista = input(f"Digite as permissões {tipo} separadas por vírgula: ").lower().strip().split(",")
        print(lista)
        if lista == [""]:
            print("A lista não pode ser vazia.")
        else:
            conjunto = set(i.strip() for i in lista)
            return conjunto

compara_conjuntos = lambda conjunto, subconjunto: subconjunto.issubset(conjunto)

def escreve_resposta(resultado: bool) -> None:
    if resultado:
        print("As permissões solicitadas fazem parte das permissões principais.")
    else:
        print("As permissões solicitadas não fazem parte das permissões principais.")

if __name__ == "__main__":
    principais = forma_lista("principais")
    solicitadas = forma_lista("solicitadas")
    resposta = compara_conjuntos(principais, solicitadas)
    escreve_resposta(resposta)

