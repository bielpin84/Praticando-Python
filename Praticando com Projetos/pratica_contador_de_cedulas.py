"""
10. Contador de cédulas únicas
Um banco está desenvolvendo um sistema para caixas eletrônicos e precisa de um programa que simule o saque de dinheiro. O caixa deve entregar o valor solicitado pelo usuário usando a menor quantidade possível de cédulas. As cédulas disponíveis são: R$ 100, R$ 50, R$ 20, R$ 10, R$ 5 e R$ 2.

Crie um programa que solicite ao usuário o valor do saque e calcule quantas cédulas de cada tipo serão necessárias para entregar o valor. O programa deve garantir que o valor solicitado seja válido (múltiplo de 2, já que não há cédulas de R$ 1) e tratar erros de entrada caso não seja digitado um valor numérico válido.

Exemplo de entrada:
Digite o valor do saque: 188

Saída esperada:
Cédulas entregues:  
1 de R$ 100  
1 de R$ 50  
1 de R$ 20  
1 de R$ 10  
0 de R$ 5  
4 de R$ 2  

Caso faça um saque de valor não inválido (ímpar):
Erro: O valor deve ser múltiplo de 2.
"""

def mostra_cedulas(notas: dict) -> None:
    print("\nCédulas disponíveis: ")
    for nota in notas:
        print(f"R$ {nota},00")

def mostra_saque(notas: dict) -> None:
    print("Cédulas entregues:")
    for nota in notas:
        print(f"{notas[nota]} de R$ {nota},00")

def verifica_saque(valor: int) -> bool:
    return valor <= 0 or valor == 1 or valor == 3

def verifica_terminal(numero: int) -> bool:
    return numero % 10 in {1, 3, 6, 8}

def calcula_saque(valor: int, notas: dict) -> dict:
    if verifica_terminal(valor):
        valor -= 4
        notas[2] += 2
    for nota in notas:        
        if valor > 0:
            notas[nota] += valor // nota
            valor %= nota
    return notas

def contador_de_cedulas():
    cedulas = {
        200: 0, 
        100: 0, 
        50: 0, 
        20 : 0, 
        10: 0, 
        5: 0, 
        2: 0}
    
    try:
        mostra_cedulas(cedulas)
        valor = int(input("\nDigite o valor do saque: "))
        if verifica_saque(valor):
            raise ValueError
        saque = calcula_saque(valor, cedulas)
        mostra_saque(saque)
    except ValueError:
        print("Digite um valor numérico válido.")

if __name__ == "__main__":
    contador_de_cedulas()