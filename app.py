from modelos.restaurante import Restaurante
from modelos.cardapio.bebida import Bebida
from modelos.cardapio.prato import Prato

restaurante_brasil = Restaurante('Brasil', 'Abrasileirada')
bebida_suco = Bebida ('Suco de manga', 5.0, 'grande')
bebida_suco.aplicar_desconto()
prato_paozinhodeQueijo = Prato('Paozinho de queijo',2.00, 'O melhor pão de queijo da cidade')
prato_paozinhodeQueijo.aplicar_desconto()
restaurante_brasil.adicionar_no_cardapio(bebida_suco)
restaurante_brasil.adicionar_no_cardapio(prato_paozinhodeQueijo)

def main():
    restaurante_brasil.exibir_cardapio


if __name__ == '__main__':
    main()