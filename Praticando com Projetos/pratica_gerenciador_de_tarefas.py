"""
9. Gerenciador de tarefas
Ana precisa de um programa simples para gerenciar suas tarefas diárias. Ela quer poder adicionar, visualizar e remover tarefas de uma lista.

Crie um programa com um menu interativo que permita ao usuário adicionar, visualizar e remover tarefas. Use uma lista para armazenar as tarefas.

Exemplo de entrada:
1. Adicionar tarefa 
2. Visualizar tarefas 
3. Remover tarefa 
4. Sair
Escolha uma opção: 1

Saída esperada:
Digite a tarefa: Estudar Python
Tarefa adicionada!

Caso selecione a opção 2 ao adicionar uma tarefa:
Tarefas:
1. Estudar Python

Caso selecione a opção 3 com uma tarefa adicionada:
Digite o número da tarefa a ser removida: 1
Tarefa 'Estudar Python' removida!

Caso selecione a opção 3 sem uma tarefa adicionada:
Digite o número da tarefa a ser removida: Estudar Python
Erro: Nenhuma tarefa para remover.

Caso selecione a opção 3 com uma opção inválida:
Digite o número da tarefa a ser removida: ABC
Erro: Entrada inválida! Digite um número.

Caso selecione nenhuma das opções listadas:
Erro: Opção inválida! Escolha uma opção entre 1 e 4.

Caso selecione a opção 4:
Escolha uma opção: 4 
Saindo do gerenciador de tarefas. Até mais!
"""

def exibir_menu() -> str:
    print("""
--------------------------------------------------
          Organizador de Tarefas da Ana
--------------------------------------------------
        
1. Adicionar tarefa
2. Visualizar tarefas
3. Remover tarefa
4. Sair
    """)
    return input("Escolha uma opção: ")

def adicionar_tarefa(tarefas: list) -> list:
    tarefa = input("Digite a tarefa: ").strip()
    if tarefa:
        tarefas.append(tarefa)
        print("Tarefa adicionada!")
    else:
        print("Erro: A tarefa não pode estar vazia.")
    return tarefas

def exibir_tarefas(tarefas: list) -> None:
    if tarefas:
        print("\nTarefas: ")
        for i, tarefa in enumerate(tarefas, 1):
            print(f"{i}. {tarefa}")
    else:
        print("Nenhuma tarefa cadastrada.")

def remover_tarefas(tarefas: list) -> list:
    if not tarefas:
        print("Erro: Nenhuma tarefa para remover.")
    else:
        try:
            exibir_tarefas(tarefas)
            remover = int(input("\nDigite o número da tarefa a ser removida: "))
            if 0 < remover <= len(tarefas):
                removida = tarefas.pop(remover-1)
                print(f"Tafera '{removida}' removida")
            else:
                print(f"Erro: Não há tarefa {remover} para remover.")
        except ValueError:
            print("Erro: Entrada inválida! Digite um número.")
    return tarefas

def gerenciador_de_tarefas(tarefas: list) -> list:
    resposta = ""
    while resposta != "4":
        resposta = exibir_menu()
        match resposta:
            case "1":
                tarefas = adicionar_tarefa(tarefas)
            case "2":
                exibir_tarefas(tarefas)
            case "3":
                tarefas = remover_tarefas(tarefas)
            case "4":
                print("Saindo do gerenciador de tarefas. Até mais!")
            case _:
                print("Erro: Opção inválida! Escolha uma opção entre 1 e 4.")
    return tarefas

if __name__ == "__main__":
    tarefas_da_ana = gerenciador_de_tarefas([])
