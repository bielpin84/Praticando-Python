"""
2. Validando um CPF
Carlos trabalha em um cartório e precisa validar se um CPF informado pelo cliente tem o formato correto antes de prosseguir com o atendimento. O CPF deve conter exatamente 11 dígitos numéricos. Se a entrada contiver letras ou qualquer outro caractere que não seja um número, o programa deve exibir uma mensagem de erro.

Crie um programa que peça ao usuário um número de CPF e verifique se ele tem 11 dígitos e contém apenas números.

Exemplo de entrada:
Digite seu CPF: 12345678901
Saída esperada:
CPF válido.
Se for inválido:
Digite seu CPF: 1234abc567
Erro: O CPF deve conter apenas números.
Se o CPF tiver um número de dígitos diferente de 11:
Digite seu CPF: 1234567  
Erro: O CPF deve ter exatamente 11 dígitos.
"""
def valida_cpf(cpf = None):
    if cpf is None:
        cpf = input("Digite o CPF (somente números): ")
    if not cpf.isdigit():
        return "Erro: O CPF deve conter apenas números."
    elif len(cpf) != 11:
        return "Erro: O CPF deve ter exatamente 11 dígitos."
    else:
        return "CPF válido."

if __name__ == "__main__":
    print(valida_cpf("12345678901"))
    print(valida_cpf("1234abc567"))
    print(valida_cpf("1234567"))