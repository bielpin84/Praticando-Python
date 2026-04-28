def calculadora_de_gorjeta(conta, porcentagem_gorjeta):
    """
    Calcula o valor da gorjeta com base no valor da conta e na porcentagem da gorjeta.

    Parâmetros:
    conta (float): O valor total da conta.
    porcentagem_gorjeta (float): A porcentagem da gorjeta a ser calculada.

    Retorna:
    float: O valor da gorjeta.
    """
    if conta < 0:
        raise ValueError("O valor da conta não pode ser negativo.")
    if porcentagem_gorjeta < 0:
        raise ValueError("A porcentagem da gorjeta não pode ser negativa.")

    gorjeta = conta * (porcentagem_gorjeta / 100)
    return gorjeta

def calcular_total_com_gorjeta(conta, porcentagem_gorjeta):
    """
    Calcula o valor total da conta incluindo a gorjeta.

    Parâmetros:
    conta (float): O valor total da conta.
    porcentagem_gorjeta (float): A porcentagem da gorjeta a ser calculada.

    Retorna:
    float: O valor total da conta incluindo a gorjeta.
    """
    gorjeta = calculadora_de_gorjeta(conta, porcentagem_gorjeta)
    total_com_gorjeta = conta + gorjeta
    return total_com_gorjeta

if __name__ == "__main__":
    valor_conta = float(input("Digite o valor da conta: "))
    porcentagem_gorjeta = float(input("Digite a porcentagem de gorjeta: "))
    gorjeta = calculadora_de_gorjeta(valor_conta, porcentagem_gorjeta)
    total_a_pagar = calcular_total_com_gorjeta(valor_conta, porcentagem_gorjeta)
    print(f"Valor da gorjeta: R$ {gorjeta:.2f}")
    print(f"Total a pagar: R$ {total_a_pagar:.2f}")