# Exercícios
"""
1 - Solicite ao usuário que insira um número e, em seguida, use uma estrutura if else para determinar se o número é par ou ímpar.
"""
def par_ou_impar(numero = None):
    try:
        if numero is None:
            numero = int(input("Digite um número inteiro: "))
        if numero % 2 == 0:
            resultado = f"O número {numero} é par"
        else:
            resultado = f"O número {numero} é ímpar"
    except:
        resultado = "Erro"
    return resultado

"""
2 - Pergunte ao usuário sua idade e, com base nisso, use uma estrutura if elif else para classificar a idade em categorias de acordo com as seguintes condições:
Criança: 0 a 12 anos;
Adolescente: 13 a 18 anos;
Adulto: acima de 18 anos.
"""
def classificando_idade(idade = None):
    try:
        if idade is None:
            idade = int(input("Digite sua idade em anos: "))
        match idade:
            case _ if 0 < idade <= 12:
                return "Criança"
            case _ if 12 < idade <= 18:
                return "Adolescente"
            case _ if idade > 18:
                return "Adulto"
            case _:
                return "Idade incorreta"
    except:
        return "Erro"

"""
3 - Solicite um nome de usuário e uma senha e use uma estrutura if else para verificar se o nome de usuário e a senha fornecidos correspondem aos valores esperados determinados por você.
"""
def confere_nome_e_senha(nome = None, senha = None):
    nome_esperado = "Gabriel"
    senha_esperada = "1234"
    if nome is None:
        nome = input("Digite o nome de usuário: ")
    if senha is None:
        senha = input("Digite a senha: ")
    if nome == nome_esperado and senha == senha_esperada:
        print("Nome e senha corretos.")
    else:
        print("Nome e/ou senha incorretos.")

"""
4 - Solicite ao usuário as coordenadas (x, y) de um ponto qualquer e utilize uma estrutura if elif else para determinar em qual quadrante do plano cartesiano o ponto se encontra de acordo com as seguintes condições:

Primeiro Quadrante: os valores de x e y devem ser maiores que zero;
Segundo Quadrante: o valor de x é menor que zero e o valor de y é maior que zero;
Terceiro Quadrante: os valores de x e y devem ser menores que zero;
Quarto Quadrante: o valor de x é maior que zero e o valor de y é menor que zero;
Caso contrário: o ponto está localizado no eixo ou origem.
"""
def descobre_coordenadas(x = None, y = None):
    try:
        if x is None:
            x = float(input('Informe o valor de x: '))
        if y is None:
            y = float(input('Informe o valor de y: '))

        match (x, y):
            case _ if x > 0 and y >0:
                print('PRIMEIRO QUADRANTE')
            case _ if x < 0 and y > 0:
                print('SEGUNDO QUADRANTE')
            case _ if x <0 and y < 0:
                print('TERCEIRO QUADRANTE')
            case _ if x > 0 and y <0:
                print('QUARTO QUADRANTE')
            case _:
                print('O PONTO ESTÁ LOCALIZADO NO EIXO DE ORIGEM')
    except Exception as e:
        print("Erro: ", e)

if __name__ == "__main__":
    if par_ou_impar(8) == "O número 8 é par" and par_ou_impar(9) == "O número 9 é ímpar" and par_ou_impar("Par") == 'Erro':
        print("A função par_ou_impar passou nos testes\n")
    else:
        print("A função par_ou_impar não passou nos testes\n")
    
    if classificando_idade(8) == "Criança" and classificando_idade(13) == "Adolescente" and classificando_idade(20) == "Adulto" and classificando_idade(-2) == "Idade incorreta" and classificando_idade("vinte") == "Erro":
        print("A função classificando_idade passou nos testes\n")
    else:
        print("A função classificando_idade não passou nos testes\n")