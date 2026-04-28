import random
import string

def gerar_senha_segura(tamanho: int = 12) -> str:
    """
    Gera uma senha com caracteres aleatórios com o formato padrão de 12 caracteres, usando letras minúsculas, maiúsculas, números e caracteres especias.
    :param: 
        tamanho (int): Quantidade de caracteres que deve ser gerado na senha, padrão de 12.
    :return: 
        str: A senha gerada.
    """
    if tamanho < 4:
        raise ValueError("O tamanho da senha deve ser pelo menos 4 para garantir a inclusão de todos os tipos de caracteres.")

    letras_maiusculas = string.ascii_uppercase
    letras_minusculas = string.ascii_lowercase
    digitos = string.digits
    caracteres_especiais = string.punctuation

    # Garantir que a senha contenha pelo menos um de cada tipo de caractere
    senha = [
        random.choice(letras_maiusculas),
        random.choice(letras_minusculas),
        random.choice(digitos),
        random.choice(caracteres_especiais)
    ]

    # Preencher o restante da senha com a mistura aleatória dos tipos de caracteres
    todos_caracteres = letras_maiusculas + letras_minusculas + digitos + caracteres_especiais
    senha.extend(random.choices(todos_caracteres, k=tamanho - 4))

    # Embaralhar a lista para evitar padrões previsíveis
    random.shuffle(senha)

    return ''.join(senha)


if __name__ == "__main__":
    tamanho_senha = int(input("Digite o tamanho da senha desejada (mínimo 4): "))
    senha_gerada = gerar_senha_segura(tamanho_senha)
    print(f"Senha segura gerada: {senha_gerada}")