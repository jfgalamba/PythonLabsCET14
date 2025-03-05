"""
Programa para gestão do catálogo de produtos. Este programa irá 
suportar operações como as em baixo indicadas:
    - Listar o catálogo
    - Pesquisar por alguns campos 
    - Eliminar um registo do catálogo
    - Guardar o catálogo em ficheiro

v1: a) Definição e utilização de um produto
"""

from decimal import Decimal as dec

class Product:
    def __init__(
            self,
            id_: int,
            name: str,
            type_: str,
            quantity: int,
            price: str,
    ):
        # 1. Validar os parâmetros do construtor
        # 2. Inicializar e definir o objecto
        self.id = id_
        self.name = name
        self.type = type_
        self.quantity = quantity
        self.price = dec(price)
    #:
#:

def main():
    # 30987,pão de milho,AL,2,1
    prod1 = Product(
        id_ = 30987,
        name = 'pão de milho',
        type_ = 'AL',
        quantity = 2,
        price = '1'
    )

    # 30098,leite mimosa,AL,10,2
    prod2 = Product(
        id_ = 30098, 
        name = 'leite mimosa',
        type_ = 'AL',
        quantity = 10, 
        price = '2'
    )

    print(f"Produto ID: {prod1.id} NOME: {prod1.name}")
    print(f"Produto ID: {prod2.id} NOME: {prod2.name}")
#:

if __name__ == '__main__':
    main()



"""
class NomeClasse:
   * variáveis/atributos/campos de classe (lá iremos...)
   * métodos: funções definidas dentro de uma classe e que operam
              sobre os atributos dos objectos
   * método construtor: método que permite definir o objecto, isto é,
                        criar e inicializar os atributos do objecto
"""

"""
Produto(30987, 'pão de milho') =>
        obj = Produto.__new__(id_, name)
        ojb = Produto.__init__(obj, id_, name)
"""
