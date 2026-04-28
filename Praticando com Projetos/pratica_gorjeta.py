"""
1. Calculando a gorjeta em um restaurante
João trabalha como garçom em um restaurante e precisa calcular a gorjeta que os clientes deixam ao pagar a conta. O restaurante sugere uma gorjeta de 10%, mas alguns clientes podem escolher dar mais ou menos.

Para agilizar o processo, João quer um programa que receba o valor total da conta e a porcentagem de gorjeta desejada e exiba o valor final que o cliente deverá pagar.

Crie um programa que peça ao usuário o valor da conta e a porcentagem de gorjeta. O programa deve calcular e exibir o valor da gorjeta e o total a ser pago.

Exemplo de entrada:
Digite o valor da conta: 120.00  
Digite a porcentagem de gorjeta: 10  
Saída esperada:
Valor da gorjeta: R$ 12.00  
Total a pagar: R$ 132.00  
"""
def calculadora_de_gorjeta(conta = None, porcentagem = None):
    """Programa que calcula a gorjeta devida diante 
    de uma conta total e uma porcentagem determinada.
    Args:
        conta (float): Valor total da conta, vem como None de padrão.
        porcentagem (float): Porcentagem da gorjeta desejada, vem como None de padrão.
    Prints:
        Valor da gorjeta
        Total a pagar
    """
    try:
        if conta is None:
            conta = float(input("Digite o valor total da conta: "))
        if porcentagem is None:
            porcentagem = float(input("Digite a porcentagem desejada para a gorjeta: "))
        gorjeta = conta * (porcentagem/100)
        total = conta + gorjeta
        return f"Valor da gorjeta: R$ {gorjeta:.2f}\nTotal a pagar: R$ {total:.2f}"
        
    except:
        return "Erro"

if __name__ == "__main__":
    print(calculadora_de_gorjeta(120, 10))