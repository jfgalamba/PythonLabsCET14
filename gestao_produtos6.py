"""
Programa para gestão do catálogo de produtos. Este programa permite:
    - Listar o catálogo
    - Pesquisar por alguns campos 
    - Eliminar um registo do catálogo
    - Guardar o catálogo em ficheiro

Trabalho realizado por:
    - Alberto Antunes
    - Armando Amaral
"""

from decimal import Decimal as dec
import subprocess
import sys
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
    # Exemplo: prod3.tipo_desc   (e não prod3.tipo() )
    @property
    def tipo_desc(self) -> str:
        return PRODUCT_TYPES[self.tipo]
    #:
#:

class InvalidProdAttr(ValueError):
    """
    Invalid Product Attribute.
    """
    pass
#:

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
        for prod in self:
            if prod.id == id_:
                return prod
        return None
    #:

    def search(self, predicate) -> 'ProductCollection':
        found = ProductCollection()
        for prod in self:
            if predicate(prod):
                found.append(prod)
        return found
    #:

    def __len__(self):
        return len(self.prods)
    #:

    def __iter__(self):
        for prod in self.prods.values():
            yield prod
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
##       MAIN E MENU PRINCIPAL E INTERACÇÃO COM O UTILIZADOR
##
################################################################################

DEFAULT_INDENTATION = 3

products: ProductCollection

def show_msg(*args, indent = DEFAULT_INDENTATION, **kargs):
    print(' ' * (indent-1), *args, **kargs)
#:

def ask(msg, indent = DEFAULT_INDENTATION) -> str:
    return input(f"{indent * ' '}{msg}")
#:

def pause(msg: str="Pressione ENTER para continuar...", indent = DEFAULT_INDENTATION):
    input(f"{' ' * indent}{msg}")
#:

def cls():
    if sys.platform == 'win32':
        subprocess.run(['cls'], shell=True, check=True)
    elif sys.platform in ('darwin', 'linux', 'bsd', 'unix'):
        subprocess.run(['clear'], check=True)
    #:
#:

def exec_menu():
    while True:
        cls()
        show_msg("*******************************************")
        show_msg("* L  - Listar catálogo                    *")
        show_msg("* P  - Pesquisar por id                   *")
        show_msg("* PT - Pesquisar por tipo                 *")
        show_msg("* A  - Acrescentar produto                *")
        show_msg("* E  - Eliminar produto                   *")
        show_msg("* G  - Guardar catálogo em ficheiro       *")
        show_msg("*                                         *")
        show_msg("* T  - Terminar programa                  *")
        show_msg("*******************************************")

        option = ask("OPÇÃO> ")

        if option.upper() in ('L', 'LISTAR'):
            exec_list_products()
        elif option.upper() in ('P', 'PESQUISAR'):
            exec_search_by_id()
        elif option.upper() in ('T', 'TERMINAR'):
            exec_end()
        else:
            show_msg(f"Opção {option} inválida ou ainda não implementada")
            pause()
#:

def exec_list_products():
    cabecalho = f'{"ID":^8}|{"Nome":^26}|{"Tipo":^8}|{"Quantidade":^16}|{"Preço":^16}'
    separador = f'{"-" * 8}+{"-" * 26}+{"-" * 8}+{"-" * 16}+{"-" * 16}'
    cls()
    show_msg("PRODUTOS")
    print()
    show_msg(cabecalho)
    show_msg(separador)
    for prod in products:
        linha = f'{prod.id:^8}|{prod.nome:^26}|{prod.tipo:^8}|{prod.quantidade:^16}|{prod.preco:^16}'
        show_msg(linha)
    print()
    pause()
#:

def exec_search_by_id():
    cabecalho = f'{"ID":^8}|{"Nome":^26}|{"Tipo":^8}|{"Quantidade":^16}|{"Preço":^16}'
    separador = f'{"-" * 8}+{"-" * 26}+{"-" * 8}+{"-" * 16}+{"-" * 16}'

    cls()
    show_msg("PESQUISA POR ID")
    print()
    while True:
        id_ = ask("Indique o ID do produto a pesquisar: ")
        if id_.isdigit():
            break
        show_msg(f"ID {id_} inválido! Tente novamente.")
    print()

    if prod := products.search_by_id(int(id_)):
        show_msg("Produto encontrado.")
        print()
        show_msg(cabecalho)
        show_msg(separador)
        linha = f'{prod.id:^8}|{prod.nome:^26}|{prod.tipo:^8}|{prod.quantidade:^16}|{prod.preco:^16}'
        show_msg(linha)
    else:
        show_msg(f"Produto com ID {id_} não encontrado.")
    
    print()
    pause()
#:

def exec_end():
    show_msg("O programa vai terminar...")
    pause()
    cls()
    sys.exit(0)
#:

def main():
    global products
    products = read_products('produtos.csv')
    exec_menu()
#:

if __name__ == '__main__':
    main()
