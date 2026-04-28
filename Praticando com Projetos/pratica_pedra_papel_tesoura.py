"""
6. Pedra, papel e tesoura
Lucas quer criar um jogo de pedra, papel e tesoura para jogar contra o computador. Ele precisa de um programa que permita ao usuário escolher uma opção e depois exiba o resultado da partida.

Crie um programa que permita ao usuário escolher entre pedra, papel ou tesoura. O computador escolherá aleatoriamente uma opção. O programa deve exibir quem venceu a partida. Lembrando que:

Pedra ganha de Tesoura (Pedra quebra Tesoura);
Tesoura ganha de Papel (Tesoura corta Papel);
Papel ganha de Pedra (Papel cobre Pedra);
Se ambos escolherem a mesma opção, é um empate.
Exemplo de entrada:
Escolha: pedra, papel ou tesoura? papel  
Saída esperada:
Computador escolheu: pedra
Você venceu!  
Caso o computador vença:
Computador escolheu: tesoura  
Você perdeu!
Caso o computador escolha a mesma opção que você:
Computador escolheu: papel 
Empate!
"""
import random

def pedra_papel_tesoura(escolha = None) -> str:
    opcoes = ["pedra", "papel", "tesoura"]
    if escolha is None:
        escolha = input("Escolha: pedra, papel ou tesoura? ")
    if escolha not in opcoes:
        return "Escolha inválida!"
    
    escolha_computador = random.choice(opcoes)
    print(f"Computador escolheu: {escolha_computador}")

    if escolha == escolha_computador:
        return "Empate!"
    elif (
        (escolha == "pedra" and escolha_computador == "tesoura") 
        or (escolha == "papel" and escolha_computador == "pedra") 
        or (escolha == "tesoura" and escolha_computador == "papel")
        ):
        return "Você venceu!"
    else:
        return "Você perdeu!"

if __name__ == "__main__":
    print(f"Escolha: pedra, papel ou tesoura? 'tesoura'\n{pedra_papel_tesoura('tesoura')}")
    print(f"Escolha: pedra, papel ou tesoura? 'pedra'\n{pedra_papel_tesoura('pedra')}")
    print(f"Escolha: pedra, papel ou tesoura? 'papel'\n{pedra_papel_tesoura('papel')}")