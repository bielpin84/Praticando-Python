"""
5. Gerador de senha segura
Pedro está desenvolvendo um sistema de cadastro e precisa gerar senhas seguras para os usuários. Ele quer um programa que crie senhas aleatórias com letras maiúsculas, minúsculas, números e caracteres especiais.

Crie um programa que gere uma senha aleatória de 12 caracteres, contendo pelo menos uma letra maiúscula, uma minúscula, um número e um caractere especial. Exiba a senha gerada.

Saída esperada:
Senha gerada: A1b@C3d$E5f&
"""
import random
import string

def gerar_senha_segura(tamanho: int = 12) -> str:
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

    # Preencher o restante da senha com uma mistura aleatória de todos os tipos de caracteres
    todos_caracteres = letras_maiusculas + letras_minusculas + digitos + caracteres_especiais
    senha += random.choices(todos_caracteres, k=tamanho - 4)

    # Embaralhar a lista para evitar padrões previsíveis
    random.shuffle(senha)

    return "".join(senha)

if __name__ == "__main__":
    print(f"Senha gerada: {gerar_senha_segura()}")