"""
Programa para gestão do catálogo de produtos. Este programa permite:
    - Listar o catálogo
    - Pesquisar por alguns campos 
    - Eliminar um registo do catálogo
    - Guardar o catálogo em ficheiro
"""

from decimal import Decimal as dec
from typing import TextIO


################################################################################
##
##       PRODUTO
##
################################################################################

CSV_DELIM = ','
PRODUCT_TYPES = {
    'AL': 'Alimentação',
    'DL': 'Detergente p/ Loiça',
    'FRL': 'Frutas e Legumes',
}

class Produto:
    def __init__(
            self,
            id_: int,           # > 0 e cinco dígitos
            nome: str,          # não pode ser vazio (ie, não pode ser '' ou '    ')
            tipo: str,          # tipo só pode ser 'AL', 'DL', 'FRL'
            quantidade: int,    # >= 0
            preco: dec,         # >= 0
    ):
        if id_ <= 0 or len(str(id_)) != 5:
            raise InvalidProdAttr(f'{id_=} inválido (deve ser > 0 e ter 5 dígitos)')

        if len(nome.strip()) == 0:
            raise InvalidProdAttr('Nome vazio')

        if tipo not in PRODUCT_TYPES:
            raise InvalidProdAttr(f'Tipo de produto inválido: {tipo}')
        
        if quantidade < 0:
            raise InvalidProdAttr('Quantidade deve ser >= 0')

        if preco < 0:
            raise InvalidProdAttr('Preço deve ser >= 0')

        self.id = id_
        self.nome = nome
        self.tipo = tipo
        self.quantidade = quantidade
        self.preco = preco
    #:

    @classmethod
    def from_csv(cls, csv: str):
        attrs = csv.split(CSV_DELIM)
        return cls(
            id_ = int(attrs[0]),
            nome = attrs[1],
            tipo = attrs[2],
            quantidade = int(attrs[3]),
            preco = dec(attrs[4]),
        )
    #:

    def __str__(self) -> str:
        cls_name = self.__class__.__name__
        return f'{cls_name}[id: {self.id} nome: {self.nome}]'
    #:

    def __repr__(self) -> str:
        cls_name = self.__class__.__name__
        return f"{cls_name}({self.id}, '{self.nome}', '{self.tipo}', {self.quantidade}, Decimal('{self.preco}'))"
    #:

    # podemos chamar este método como se fosse um atributo
    # Exemplo: prod3.tipo_desc   (e não prod3.tipo_desc() )
    @property
    def tipo_desc(self) -> str:
        return PRODUCT_TYPES[self.tipo]
    #:
#:

class InvalidProdAttr(ValueError):
    """
    Invalid Product Attribute.
    """
#:


"""
try:
    raise InvalidProdAttr('dadas')
except InvalidProdAttr:
    pass
except ValueError:
    pass
"""

"""
from typing import override

class A:
    def __init__(self, x: int):
        self.x = x
    def metodo1(self, w: int) -> int:
        return 2 * self.x + w


class B(A):     # A -> superclasse   B -> subclasse
    @override
    def metodo1(self, w: int) -> int:
        return 3 * self.x + w

class C(A):     # A -> superclasse   C -> subclasse
    def __init__(self, x: int, y: int):
        super().__init__(x)
        self.y = y
    @override
    def metodo1(self, w: int) -> int:
        return super().metodo1(w) + self.y
  A
  |
  +----- B
  +----- C
"""
################################################################################
##
##       CATÁLOGO DE PRODUTOS (PRODUCT COLLECTION)
##
################################################################################

class ProductCollection:
    def __init__(self):
        self.prods = {}
    #:

    def append(self, prod: Produto):
        if prod.id in self.prods:
            raise DuplicateValue(f'Já existe produto com id {prod.id} na colecção')
        self.prods[prod.id] = prod
    #:

    def search_by_id(self, id_: int) -> Produto | None:
        for prod in self.prods:
            if prod.id == id_:
                return prod
        return None
    #:

    def _dump(self):
        for prod in self.prods.values():
            print(prod)
    #:
#:

class DuplicateValue(Exception):
    pass
#:

################################################################################
##
##       I/O: LEITURA E ESCRITA DA BD DE PRODUTOS
##
################################################################################

def read_products(in_file_path: str) -> ProductCollection:
    products = ProductCollection()
    with open(in_file_path, 'rt') as in_file:
        for line in relevant_lines(in_file):
            products.append(Produto.from_csv(line))
    return products
#:

def relevant_lines(file: TextIO):
    for line in file:
        line = line.strip()
        if len(line) == 0:
            continue
        if line.startswith('#'):
            continue
        yield line   # TODO: remover '\n'
#:

################################################################################
##
##       MAIN E MENU PRINCIPAL
##
################################################################################

products: ProductCollection

def main():
    global products
    products = read_products('produtos.csv')
    products._dump()
#:

if __name__ == '__main__':
    main()
