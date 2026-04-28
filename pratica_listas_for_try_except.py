"""
1 - Crie uma lista para cada informação a seguir:

Lista de números de 1 a 10;
Lista com quatro nomes;
Lista com o ano que você nasceu e o ano atual.
"""
numeros_de_1_a_10 = [i for i in range(1, 11)]
quatro_nomes = ["Ana", "José", "Thiago", "Aurora"]
ano_nasceu_ano_atual = [1984, 2026]
"""
2 - Crie uma lista e utilize um loop for para percorrer todos os elementos da lista.
"""
for i in numeros_de_1_a_10:
    print(i)
"""
3 - Utilize um loop for para calcular a soma dos números ímpares de 1 a 10.
"""
soma = 0
for i in numeros_de_1_a_10:
    if i % 2 == 0:
        pass
    else:
        soma += i
print(soma)
"""
4 - Utilize um loop for para imprimir os números de 1 a 10 em ordem decrescente.
"""
for i in numeros_de_1_a_10[::-1]:
    print(i)
"""
5 - Solicite ao usuário um número e, em seguida, utilize um loop for para imprimir a tabuada desse número, indo de 1 a 10.
"""
numero = int(input("Digite um número inteiro de 1 a 10: "))
print(f"\nA Tabuada de {numero} é:")
for i in numeros_de_1_a_10:
    print(f"{numero} vezes {i} = {numero*i}")
"""
6 - Crie uma lista de números e utilize um loop for para calcular a soma de todos os elementos. Utilize um bloco try-except para lidar com possíveis exceções.
"""
lista_de_numeros = [i for i in range(13, 100, 17)]
print(lista_de_numeros)
lista_errada = [13, 14, "quinze", 16]

def soma_lista(lista: list) -> int:
    try:
        return sum(lista)
    except:
        print("Erro")
        return 0

print(soma_lista(lista_de_numeros))
print(soma_lista(lista_errada))

"""
7 - Construa um código que calcule a média dos valores em uma lista. Utilize um bloco try-except para lidar com a divisão por zero, caso a lista esteja vazia.
"""
lista_vazia = []

def calcula_a_media(lista: list) -> float:
    try:
        return sum(lista)/len(lista)
    except:
        print("Erro")
        return 0

print(calcula_a_media(lista_de_numeros))
print(calcula_a_media(lista_vazia))