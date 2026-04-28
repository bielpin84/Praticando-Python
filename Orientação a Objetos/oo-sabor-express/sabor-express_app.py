from modelos.restaurante import Restaurante
from modelos.cardapio.prato import Prato
from modelos.cardapio.bebidas import Bebida

restaurante_praca = Restaurante("praça", "Gourmet")
bebida_suco = Bebida("suco de laranja", 8.50, "500ml")
prato_pasta = Prato("pasta italiana", 25.00, "Massa com molho especial")
restaurante_praca.adicionar_no_cardapio(bebida_suco)
restaurante_praca.adicionar_no_cardapio(prato_pasta)

def main():
    restaurante_praca.exibir_cardapio

if __name__ == "__main__":
    main()