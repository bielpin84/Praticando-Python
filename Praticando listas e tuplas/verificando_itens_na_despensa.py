"""
Roberto está organizando sua despensa e quer verificar se determinados itens já estão armazenados antes de adicioná-los à lista de compras.

Ajude Roberto a criar um programa que pergunte o item desejado e verifique se ele está na lista de itens disponíveis na despensa. Caso o item não esteja na lista, o programa deve informar que ele precisa ser comprado.

Exemplo de Entrada:

Digite o item que você quer verificar: açúcar

Saída esperada:

O item açúcar precisa ser comprado.
"""
despensa = ["macarrão", "atum", "arroz", "feijão"]
item = input("Digite o item desejado: ").strip().lower()
if not item:
    print("Você deve digitar um item.")
else:
    if item in despensa:
        print(f"O item {item} já está na despensa.")
    else:
        print(f"O item {item} precisa ser comprado.")