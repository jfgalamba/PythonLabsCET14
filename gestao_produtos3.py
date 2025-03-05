"""
Programa para gestão do catálogo de produtos. Este programa irá 
suportar operações como as em baixo indicadas:
    - Listar o catálogo
    - Pesquisar por alguns campos 
    - Eliminar um registo do catálogo
    - Guardar o catálogo em ficheiro

v3: a) Validações como @staticmethod
    b) Construtor alternativo com @classmethod (+ delimitador ',')
    c) Método para gerar CSV
    d) @property para desc do tipo
"""

from decimal import Decimal as dec


CSV_DELIM = ','

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

    @property
    def type_desc(self) -> str:
        return Product.PRODUCT_TYPE[self.type]
    #:

    @classmethod
    def from_csv(cls, csv: str, delim = CSV_DELIM) -> 'Product':
        attrs = csv.split(delim)
        return Product(
            id_ = int(attrs[0]),
            name = attrs[1],
            type_ = attrs[2],
            quantity = int(attrs[3]),
            price = attrs[4],
        )
    #:

    def to_csv(self, delim = CSV_DELIM) -> str:
        return delim.join([
                str(self.id),
                self.name,
                self.type,
                str(self.quantity),
                str(self.price),
        ])
        # return f'{self.id}{delim}{self.name}{delim}{self.type}{delim}{self.quantity}{delim}{self.price}'
    #:

    def show(self):
        print(f"PRODUTO ID => {self.id}")
        print(f"Nome       : {self.name}")
        print(f"Tipo       : {self.type}")
        print(f"Preço      : {self.price}")
        print(f"Quantidade : {self.quantity}")
    #:

    @staticmethod
    def validate_name(full_name: str) -> bool:
        names = full_name.split()
        return len(names) >= 2 and all(len(name) >= 2 and name.isalpha() for name in names)
    #:
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

        # 40001,morangos da escócia,FRL,100,1.5
        prod3 = Product.from_csv('40001,morangos da escócia,FRL,100,1.5')

        prod1.show()
        print()
        prod2.show()
        print()
        prod3.show()
        print()
        print(f"prod1.to_csv(): {prod1.to_csv()}")

        print("Alguns atributos de prod2:")
        print("ID   :", prod2.id)
        print("Tipo :", prod2.type_desc)

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
