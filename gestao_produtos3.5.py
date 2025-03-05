"""
Programa para gestão do catálogo de produtos. Este programa permite:
    - Listar o catálogo
    - Pesquisar por alguns campos 
    - Eliminar um registo do catálogo
    - Guardar o catálogo em ficheiro
"""

from decimal import Decimal as dec

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

class ProdutoPromocao(Produto):
    def __init__(self, *args, desconto: dec = dec('0'), **kargs):
        super().__init__(*args, **kargs)
        self.desconto = desconto
    #:
#:

def main():
    try:
        prod1 = Produto(
            id_ = 30987,
            nome = 'pão de milho',
            tipo = 'AL',
            quantidade = 2,
            preco = dec('1'),
        )

        prod2 = Produto(
            id_ = 30098,
            nome = 'Leite mimosa',
            tipo = 'AL',
            quantidade = 10,
            preco = dec('2'),
        )


        prod3 = Produto.from_csv('40001,morangos da escócia,FRL,100,1.5')

        print(prod1)
        print(prod2)
        print(prod3)

        # print(f"Produto ID: {prod1.id} NOME: {prod1.nome} ")
        # print(f"Produto ID: {prod2.id} NOME: {prod2.nome} ")
        # print(f"Produto ID: {prod3.id} NOME: {prod3.nome} ")
    except InvalidProdAttr as ex:
        print("ERRO: atributo inválido!")
        print(ex)
#:

if __name__ == '__main__':
    main()


