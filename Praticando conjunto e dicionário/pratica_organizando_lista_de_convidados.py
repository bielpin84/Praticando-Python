"""
Ana está organizando uma festa de aniversário e precisa de uma lista de convidados que não tenha repetições , pois algumas pessoas foram convidadas mais de uma vez por engano. Ela gostaria que o programa solicitasse o nome dos convidados e, ao final, exibisse a lista organizada sem repetições.

Escreva um programa que receba os nomes dos convidados até que o usuário digite 'sair', e ao final mostre a lista de convidados sem repetições.

Exemplo de entrada:

Digite o nome do convidado: Ana 

Digite o nome do convidado: João 

Digite o nome do convidado: Ana 

Digite o nome do convidado: Carla 

Digite o nome do convidado: sair 

Saída esperada:

Convidados confirmados: Ana, João, Carla 
"""
def forma_lista_de_convidados() -> set:
    conjunto = set()
    while True:
        nome = input("Digite o nome do convidado: ").strip().title()
        if not nome or nome.isdigit():
            print("Digite um nome válido.")
        elif nome == "Sair":
            return conjunto
        else:
            conjunto.add(nome)

def mostra_iteravel_em_ordem(iteravel) -> None:
    try:
        for indice, item in enumerate(iteravel, start=1):
            print(f"{indice}: {item}")
    except TypeError as e:
        print(f"Erro: objeto não iterável.")

if __name__ == "__main__":
    convidados = forma_lista_de_convidados()
    print("\nConvidados confirmados:")
    mostra_iteravel_em_ordem(convidados)

