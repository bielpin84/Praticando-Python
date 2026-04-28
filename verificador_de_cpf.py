cpf_usuario = input("Digite o CPF (somente números): ")
def calcular_digito(cpf_parcial):
    """Calcula o dígito verificador para o CPF parcial fornecido."""
    soma = 0
    peso = len(cpf_parcial) + 1
    for digito in cpf_parcial:
        soma += int(digito) * peso
        peso -= 1
    resto = soma % 11
    if resto < 2:
        return '0'
    else:
        return str(11 - resto)

def validar_cpf(cpf):
    """Valida o CPF fornecido."""
    if len(cpf) != 11 or not cpf.isdigit():
        return False
    cpf_parcial = cpf[:9]
    primeiro_digito = calcular_digito(cpf_parcial)
    segundo_digito = calcular_digito(cpf_parcial + primeiro_digito)
    return cpf == cpf_parcial + primeiro_digito + segundo_digito

if __name__ == "__main__":
    if validar_cpf(cpf_usuario):
        print("CPF válido.")
    else:
        print("CPF inválido.")
