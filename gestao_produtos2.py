"""
Programa para gestão do catálogo de produtos. Este programa irá 
suportar operações como as em baixo indicadas:
    - Listar o catálogo
    - Pesquisar por alguns campos 
    - Eliminar um registo do catálogo
    - Guardar o catálogo em ficheiro

v2: a) Definir o método show
    b) Validar parâmetros c/ excepções
"""

from decimal import Decimal as dec


class Product:
    PRODUCT_TYPE = {
        'AL': 'Alimentação',
        'DL': 'Detergentes p/ Louça',
        'FRL': 'Frutas e Legumes',
    }

    def __init__(
            self,
            id_: int,           # > 0 e cinco dígitos
            name: str,          # tem que conter duas ou mais palavras c/ 2 caracteres
            type_: str,         # só poder um de 'AL', 'DL', 'FRL'
            quantity: int,      # >= 0
            price: str,         # >= 0
    ):
        # 1. Validar os parâmetros do construtor
        if id_ <= 0 or len(str(id_)) != 5:
            raise InvalidAttrValue(f'{id_=} inválido: deve ser > 0 e ter 5 dígitos')

        if not self.validate_name(name.strip()):
            raise InvalidAttrValue(f'Nome inválido: {name}')

        if type_ not in Product.PRODUCT_TYPE:
            raise InvalidAttrValue(f'Tipo de produto inválido: {type_}')

        if quantity < 0:
            raise InvalidAttrValue('Quantidade deve ser >= 0')

        if dec(price) < 0:
            raise InvalidAttrValue('Preço deve ser >= 0')

        # 2. Inicializar e definir o objecto
        self.id = id_
        self.name = name.strip()
        self.type = type_
        self.quantity = quantity
        self.price = dec(price)
    #:

    def show(self):
        print(f"PRODUTO ID => {self.id}")
        print(f"Nome       : {self.name}")
        print(f"Tipo       : {self.type}")
        print(f"Preço      : {self.price}")
        print(f"Quantidade : {self.quantity}")
    #:

    def validate_name(self, full_name: str) -> bool:
        names = full_name.split()
        if len(names) < 2:
            return False
        return all(len(name) >= 2 and name.isalpha() for name in names)
    #:

    # def validate_name(self, full_name: str) -> bool:
    #     names = full_name.split()
    #     if len(names) < 2:
    #         return False
    #     for name in names:
    #         if len(name) < 2 or not name.isalpha():
    #             return False
    #     return True
    # #:
#:

class InvalidAttrValue(ValueError):
    """
    Valor para atributo inválido
    """

def main():
    try:
        # 30987,pão de milho,AL,2,1
        prod1 = Product(
            id_ = 30987,
            name = 'Alberto Al Fl',
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

        prod1.show()   # Produto.show(prod1)
        print()
        prod2.show()   # Produto.show(prod2)

    except ValueError as ex:
        print("Problemas ao criar produto:")
        print(ex)
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
