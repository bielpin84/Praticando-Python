# Aquecimento
'''
1. Faça um programa que solicite à pessoa usuária digitar dois números float e calcular a divisão entre esses números. O código deve conter um tratamento de erro, indicando o tipo de erro que foi gerado caso a divisão não seja possível de realizar.

Teste o programa com o segundo valor numérico do input igual a 0. Também teste utilizando caracteres textuais no input para checar os tipos de erro que ocorrem.
'''
def exercicio1():
    print("Exercício 1:")
    try:
        numero1 = float(input("Digite o primeiro número: "))
        numero2 = float(input("Digite o segundo número: "))
        print(f"O resultado da divisão é: {numero1 / numero2}")
    except Exception as e:
        print(f"Ocorreu um erro ao realizar a divisão: {e}")
# exercicio1()

'''
2. Faça um programa que solicite à pessoa usuária digitar um texto que será uma chave a ser pesquisada no seguinte dicionário: idades = {'Júlia': 16, 'Carol': 23, 'Alberto': 19, 'Roberta': 17}, armazenando o resultado do valor em uma variável. O código deve conter um tratamento de erro KeyError, imprimindo a informação 'Nome não encontrado', caso ocorra o erro; e imprimir o valor caso não ocorra nenhum.

Teste o programa com um nome presente em uma das chaves do dicionário e com um que não esteja no dicionário para verificar a mensagem de erro.
'''
def exercicio2():
    print("Exercício 2:")
    idades = {'Júlia': 16, 'Carol': 23, 'Alberto': 19, 'Roberta': 17}
    nome = input("Digite um nome para pesquisar a idade: ")
    try:
        idade = idades[nome]
        print(f"A idade de {nome} é {idade} anos.")
    except KeyError:
        print("Nome não encontrado.")
# exercicio2()

'''
3. Crie uma função que recebe uma lista como parâmetro e converta todos os valores da lista para float. A função deve conter um tratamento de erro indicando o tipo de erro gerado e retornar a lista caso não tenha ocorrido nenhum erro. Por fim, deve ter a cláusula finally para imprimir o texto: 'Fim da execução da função'.
'''
def exercicio3():
    print("Exercício 3:")
    def converter_cada_item_para_float(lista: list):
        lista_convertida = []
        try:
            for item in lista:
                numero = float(item)
                lista_convertida.append(numero)
        except Exception as e:
            print(f"Erro do tipo {type(e).__name__}: {e}")
        else:
            print(lista_convertida)
        finally:
            print("Fim da execução da função")
    lista1 = ['1.5', '2.3', '3.1', '4.7']
    lista2 = ['5.6', 'seis', '7.8', 'nove']
    print("Convertendo lista1:")
    converter_cada_item_para_float(lista1)
    print("Convertendo lista2:")
    converter_cada_item_para_float(lista2)
# exercicio3()

'''
4. Crie uma função que recebe duas listas como parâmetros e agrupe os elementos um a um das listas, formando uma lista de tuplas de 3 elementos, no qual o primeiro e segundo elemento da tupla são os valores na posição i das listas e o terceiro elemento é a soma dos valores na posição i das listas.

A função deve conter um tratamento de erro indicando o tipo de erro gerado e retornar como resultado a lista de tuplas. Caso as listas enviadas como parâmetro tenham tamanhos diferentes, a função deve retornar um IndexError com a frase: 'A quantidade de elementos em cada lista é diferente.' Dados para testar a função:

Valores sem erro:
lista1 = [4,6,7,9,10]
lista2 = [-4,6,8,7,9]
Listas com tamanhos diferentes:
lista1 = [4,6,7,9,10,4]
lista2 = [-4,6,8,7,9]
Listas com valores incoerentes:
lista1 = [4,6,7,9,'A']
lista2 = [-4,'E',8,7,9]
'''
def exercicio4():
    print("Exercício 4:")
    def forma_lista_de_tuplas(lista1: list, lista2: list) -> list:
        lista_de_tuplas = []
        try:
            if len(lista1) != len(lista2):
                raise IndexError("A quantidade de elementos em cada lista é diferente.")
            for i in range(len(lista1)):
                tupla = (lista1[i], lista2[i], lista1[i] + lista2[i])
                lista_de_tuplas.append(tupla)
        except Exception as e:
            print(f"Erro do tipo {type(e).__name__}: {e}")
        else:
            return lista_de_tuplas
        finally:
            print("Fim da execução da função")
            
    for i in range(1,4):
        print(f"Teste {i}:")
        match i:
            case 1:
                lista1 = [4,6,7,9,10]
                lista2 = [-4,6,8,7,9]
            case 2:
                lista1 = [4,6,7,9,10,4]
                lista2 = [-4,6,8,7,9]
            case 3:
                lista1 = [4,6,7,9,'A']
                lista2 = [-4,'E',8,7,9]
        print("Lista 1:", lista1)
        print("Lista 2:", lista2)
        resultado = forma_lista_de_tuplas(lista1, lista2)
        if resultado:
            print("Lista de tuplas resultante:", resultado)
# exercicio4()

# Aplicando a projetos
'''
5. Como desafio, você recebeu a tarefa de desenvolver um código que contabiliza as pontuações de estudantes de uma instituição de ensino de acordo com suas respostas num teste. Este código deve ser testado para um exemplo de 3 estudantes com uma lista de listas em que cada lista possui as respostas de 5 questões objetivas de cada estudante. Cada questão vale um ponto e as alternativas possíveis são A, B, C ou D.

Caso alguma alternativa em um dos testes não esteja entre as alternativas possíveis, você deve lançar um ValueError com a mensagem "A alternativa [alternativa] não é uma opção de alternativa válida". O cálculo das 3 notas só será realizado mediante as entradas com as alternativas A, B, C ou D em todos os testes. Se não for lançada a exceção, será exibida uma lista com as notas em cada teste.

Os dados para o teste do código são:

Gabarito da prova:
gabarito = ['D', 'A', 'B', 'C', 'A']
Abaixo temos 2 listas de listas que você pode usar como teste

Notas sem exceção:
testes_sem_ex = [['D', 'A', 'B', 'C', 'A'], ['C', 'A', 'A', 'C', 'A'], ['D', 'B', 'A', 'C', 'A']]
Notas com exceção:
testes_com_ex = [['D', 'A', 'B', 'C', 'A'], ['C', 'A', 'A', 'E', 'A'], ['D', 'B', 'A', 'C', 'A']]
Dica: Para verificar se uma entrada da lista não está entre as alternativas possíveis, use a estrutura lista[i] not in ['A','B','C','D']. Por exemplo, 1 not in [2,3,4]... Saída: True.
'''
def exercicio5():
    print("Exercício 5:")
    def calcular_notas(gabarito: list, respostas: list[list]) -> list:
        notas = []
        try:
            for resposta in respostas:
                for alternativa in resposta:
                    if alternativa not in ['A','B','C','D']:
                        raise ValueError(f"A alternativa {alternativa} não é uma opção de alternativa válida")
                nota = sum(1 for i in range(len(gabarito)) if resposta[i] == gabarito[i])
                notas.append(nota)
        except Exception as e:
            print(f"Erro do tipo {type(e).__name__}: {e}")
        else:
            return notas
        finally:
            print("Fim da execução da função")
    gabarito = ['D', 'A', 'B', 'C', 'A']
    testes_sem_ex = [['D', 'A', 'B', 'C', 'A'], ['C', 'A', 'A', 'C', 'A'], ['D', 'B', 'A', 'C', 'A']]
    testes_com_ex = [['D', 'A', 'B', 'C', 'A'], ['C', 'A', 'A', 'E', 'A'], ['D', 'B', 'A', 'C', 'A']]
    print("Testando sem exceção:")
    notas1 = calcular_notas(gabarito, testes_sem_ex)
    if notas1:
        print("Notas dos estudantes:", notas1)
    print("Testando com exceção:")
    notas2 = calcular_notas(gabarito, testes_com_ex)
    if notas2:
        print("Notas dos estudantes:", notas2)
# exercicio5()

'''
6. Você está trabalhando com processamento de linguagem natural (NLP) e, dessa vez, sua líder requisitou que você criasse um trecho de código que recebe uma lista com as palavras separadas de uma frase gerada pelo ChatGPT.

Você precisa criar uma função que avalia cada palavra desse texto e verificar se o tratamento para retirar os símbolos de pontuação (',' '.', '!' e '?') foi realizado. Caso contrário, será lançada uma exceção do tipo ValueError apontando o 1º caso em que foi detectado o uso de uma pontuação por meio da frase "O texto apresenta pontuações na palavra "[palavra]".". Essa demanda é voltada para a análise do padrão de frases geradas pela inteligência artificial.

Dica: Para verificar se uma ou mais das pontuações estão presentes em cada palavra, utilize a palavra chave or na condição if. Por exemplo, 'a' in 'alura' or 'b' in 'alura'… Saída: True

Os dados para o teste do código são:

Lista tratada:
lista_tratada = ['Python', 'é', 'uma', 'linguagem', 'de', 'programação', 'poderosa', 'versátil', 'e', 'fácil', 'de', 'aprender', 'utilizada', 'em', 'diversos', 'campos', 'desde', 'análise', 'de', 'dados', 'até', 'inteligência', 'artificial']

Lista não tratada:
lista_nao_tratada = ['Python', 'é', 'uma', 'linguagem', 'de', 'programação', 'poderosa,', 'versátil', 'e', 'fácil,', 'de', 'aprender', 'utilizada', 'em', 'diversos', 'campos,', 'desde', 'análise', 'de', 'dados', 'até', 'inteligência', 'artificial!']
'''
def exercicio6():
    print("Exercício 6:")
    def avalia_lista_de_palavra_sobre_pontuacao(lista_de_palavras: list) ->  bool:
        try:
            for palavra in lista_de_palavras:
                if any(char in '.,!?' for char in palavra):
                    raise ValueError(f"O texto apresenta pontuações na palavra '{palavra}'.")
        except Exception as e:
            print(f"Erro do tipo {type(e).__name__}: {e}")
        else:
            return True
        finally:
            print("Fim da execução da função")
    lista_tratada = ['Python', 'é', 'uma', 'linguagem',
                     'de', 'programação', 'poderosa', 'versátil', 'e', 'fácil', 'de','aprender', 'utilizada', 'em','diversos', 'campos', 'desde',
                     'análise', 'de', 'dados', 'até', 'inteligência', 'artificial']
    lista_nao_tratada = ['Python', 'é', 'uma',
                         'linguagem', 'de', 'programação', 'poderosa,', 'versátil', 'e', 'fácil,', 'de', 'aprender', 'utilizada', 'em', 'diversos', 'campos,', 'desde',
                         'análise', 'de', 'dados', 'até',
                         'inteligência', 'artificial!']
    print("Testando lista tratada:")
    resultado1 = avalia_lista_de_palavra_sobre_pontuacao(lista_tratada)
    if resultado1:
        print("A lista está livre de pontuações.")
    print("Testando lista não tratada:")
    resultado2 = avalia_lista_de_palavra_sobre_pontuacao(lista_nao_tratada)
    if resultado2:
        print("A lista está livre de pontuações.")
# exercicio6()

'''
7. Você foi contratado(a) como uma pessoa cientista de dados para auxiliar um laboratório que faz experimentos sobre o comportamento de uma cultura de fungos. O laboratório precisa avaliar constantemente a razão (divisão) entre os dados de pressão e temperatura do ambiente controlado recolhidos durante a experimentação para definir a melhor condição para os testes.
Para cumprir com a demanda, você precisa criar uma função divide_colunas que recebe os dados das colunas de pressão e temperatura (que vem no formato de listas) e gerar uma nova coluna com o resultado da divisão. Os parâmetros da função são as duas listas e você deve tratar dentro dela ao menos 2 tipos de exceções:

Verificar se as listas têm o mesmo tamanho (ValueError)
Verificar se existe alguma divisão por zero (ZeroDivisionError)
Para testar a função, vamos realizar a divisão entre duas listas de dados coletados no experimento, com os valores de pressão e temperatura do ambiente controlado.

Como teste, use os seguintes dados:

Dados sem exceção:
pressoes = [100, 120, 140, 160, 180]
temperaturas = [20, 25, 30, 35, 40]

Dados com exceção:
1) Exceção de ZeroDivisionError
pressoes = [60, 120, 140, 160, 180]
temperaturas = [0, 25, 30, 35, 40]
2) Exceção de ValueError
pressoes = [100, 120, 140, 160]
temperaturas = [20, 25, 30, 35, 40]
Dica: Você pode usar zip() para parear os dados da lista_1 com a lista_2. Crie uma estrutura try-except que caso uma das exceções sejam lançadas, podemos ver o tipo de erro na saída.
'''
def exercicio7():
    print("Exercício 7:")
    def calcula_razao_pressao_temperatura(pressao: list, temperatura: list) -> list:
        razoes = []
        try:
            if len(pressao) != len(temperatura):
                raise ValueError("As listas de pressão e temperatura devem ter o mesmo tamanho.")
            for p, t in zip(pressao, temperatura):
                razao = p / t
                razoes.append(razao)
        except Exception as e:
            print(f"Erro do tipo {type(e).__name__}: {e}")
        else:
            return razoes
        finally:
            print("Fim da execução da função")
    # Teste sem exceção
    pressoes1 = [100, 120, 140, 160, 180]
    temperaturas1 = [20, 25, 30, 35, 40]
    print("Testando sem exceção:")
    razoes1 = calcula_razao_pressao_temperatura(pressoes1, temperaturas1)
    if razoes1:
        print("Razões pressão/temperatura:", razoes1)
    # Teste com ZeroDivisionError
    pressoes2 = [60, 120, 140, 160, 180]
    temperaturas2 = [0, 25, 30, 35, 40]
    print("Testando com ZeroDivisionError:")
    razoes2 = calcula_razao_pressao_temperatura(pressoes2, temperaturas2)
    if razoes2:
        print("Razões pressão/temperatura:", razoes2)
    # Teste com ValueError
    pressoes3 = [100, 120, 140, 160]
    temperaturas3 = [20, 25, 30, 35, 40]
    print("Testando com ValueError:")
    razoes3 = calcula_razao_pressao_temperatura(pressoes3, temperaturas3)
    if razoes3:
        print("Razões pressão/temperatura:", razoes3)
# exercicio7()