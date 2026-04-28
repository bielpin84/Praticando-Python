"""
Laura e Ana resolveram fazer compras juntas, mas criaram duas listas diferentes. Elas querem um programa que mostre:
Quais itens apareceram nas duas listas
Quais foram exclusivos de Laura
Quais foram exclusivos da Ana

Escreva um programa que solicite as listas e mostre os resultados dessas comparações.

Exemplo de entrada:
Lista de Laura: leite, pão, café, açúcar 
Lista de Ana: pão, café, biscoito, chocolate 

Saída esperada:
Itens em ambas as listas: pão, café 
Itens exclusivos de Laura: leite, açúcar 
Itens exclusivos de Ana: biscoito, chocolate 
"""
def forma_lista():
    while True:
        lista = input("Digite a lista de compras separada por vírgula: ").strip()
        if not lista:
            print("A lista de compras não pode ser vazia.")
        else:
            return set(lista.split(", "))

lista_em_string = lambda iteravel: f"{', '.join(iteravel)}"

lista_laura = forma_lista()
lista_ana = forma_lista()
itens_em_ambas = lista_laura & lista_ana
exclusivos_laura = lista_laura - lista_ana
exclusivos_ana = lista_ana - lista_laura

print(f"Itens em ambas as listas: {lista_em_string(itens_em_ambas)}")
print(f"Itens exclusivos de Laura: {lista_em_string(exclusivos_laura)}")
print(f"Itens exclusivos de Ana: {lista_em_string(exclusivos_ana)}")

