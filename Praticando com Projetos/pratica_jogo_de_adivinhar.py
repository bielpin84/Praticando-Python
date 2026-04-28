"""
7. Jogo de adivinhar o número
Maria está criando um jogo para seus alunos praticarem lógica e pensamento rápido. Ela quer um programa onde o computador escolhe um número aleatório entre 1 e 100, e o jogador tem que adivinhar qual é.

Além de garantir a jogabilidade, Maria deseja que o programa trate erros de entrada, impedindo que o usuário forneça valores inválidos, como letras ou números fora do intervalo permitido.

Sua tarefa é criar um programa que gere um número aleatório entre 1 e 100 e permita que o usuário tente adivinhar o número. O programa deve informar se o palpite é maior ou menor que o número correto, até que o usuário acerte. Se o usuário digitar um valor inválido ou um número fora do intervalo, uma exceção ValueError deve ser lançada .

Exemplo de entrada:
Tente adivinhar o número (1-100): 50  
Saída esperada:
Parabéns! Você acertou o número 37.  
Caso o número esteja abaixo:
Muito baixo! Tente novamente: 17   
Agora, caso esteja acima:
Muito alto! Tente novamente: 75    
Em caso de exceção:
Entrada inválida: Número fora do intervalo! Digite um número entre 1 e 100.
Entrada inválida: invalid literal for int() with base 10: 'abc12
"""
import random

def jogo_adivinhacao():
    numero = random.randint(1,100)

    while True:
        try:
            palpite = int(input("Tente adivinhar o número (1-100): "))

            if 1 < palpite > 100:
                raise ValueError("Número fora do intervalo! Digite um número entre 1 e 100.")
            
            if palpite > numero:
                print(f"Muito alto! Tente novamente: {palpite}")
            elif palpite < numero:
                print(f"Muito baixo! Tente novamente: {palpite}")
            else:
                print(f"Parabéns! Você acertou o número: {palpite}")
                break
        except Exception as e:
            print(f"Entrada inválida: {e}")

if __name__ == "__main__":
    jogo_adivinhacao()