"""
8. Calculadora com tratamento de erros
Carlos está criando uma calculadora simples, mas quer garantir que o programa não quebre se o usuário digitar valores inválidos, ele precisa tratar os erros.

Crie uma calculadora que permita ao usuário escolher entre soma, subtração, multiplicação e divisão. Além de modularizar o código em funções, use try-except para tratar erros de entrada inválida, que consiste em:

Caso digite um caractere em vez de número | exceção a ser lançada: ValueError;
Caso tente fazer uma divisão por 0 | exceção a ser lançada: ZeroDivisionError.

Exemplo de entrada:
Digite o primeiro número: 5
Escolha a operação (+, -, *, /): +
Digite o segundo número: 7

Saída esperada:
Resultado: 12

Caso selecione nenhuma das operações listadas:
Opção inválida

Caso digite um caractere em vez de número:
Erro: Entrada inválida. Digite apenas números.

Caso tente fazer uma divisão por 0:
Erro: Divisão por zero não é permitida.
"""
def calculadora_simples():
    try:
        primeiro_numero = float(input("Digite o primeiro número: "))
        operacao = input("Escolha a operação (+, -, *, /): ")
        segundo_numero = float(input("Digite o segundo número: "))
        match operacao:
            case "+":
                resultado = primeiro_numero + segundo_numero
            case "-":
                resultado = primeiro_numero - segundo_numero
            case "*":
                resultado = primeiro_numero * segundo_numero
            case "/":
                if segundo_numero == 0:
                    raise ZeroDivisionError
                resultado = primeiro_numero / segundo_numero
            case _:
                return "Opção inválida"
        
        return f"Resultado: {resultado}"
    
    except ValueError:
        return "Erro: Entrada inválida. Digite apenas números."
    except ZeroDivisionError:
        return "Erro: Divisão por zero não é permitida."

if __name__ == "__main__":
    print(calculadora_simples())