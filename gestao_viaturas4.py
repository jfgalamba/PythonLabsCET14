"""
Programa para gestão do catálogo de viaturas. Este programa permitirá:
    - Listar o catálogo
    - Pesquisar por alguns campos 
    - Eliminar um registo do catálogo
    - Guardar o catálogo em ficheiro
"""

from datetime import date
from typing import TextIO


################################################################################
##
##       VIATURA
##
################################################################################

CSV_DELIM = '|'

class Viatura:
    def __init__(
            self,
            matricula: str,          # matricula: DD-LL-DD onde D: Dígito L: Letra
            marca: str,              # deve ter uma ou mais palavras (apenas letras ou dígitos)
            modelo: str,             # mesmo que a marca
            data: str,               # deve vir no formato ISO: 'YYYY-MM-DD'
    ):
        if not valida_matricula(matricula):
            raise InvalidProdAttr(f'Matrícula inválida: {matricula}')

        if not valida_marca(marca):
            raise InvalidProdAttr(f'Marca inválida: {marca}')

        if not valida_modelo(modelo):
            raise InvalidProdAttr(f'Modelo inválido: {modelo}')

        self.matricula = matricula
        self.marca = marca
        self.modelo = modelo
        self.data = date.fromisoformat(data)
    #:

    @classmethod
    def from_csv(cls, csv: str) -> 'Viatura':
        attrs = csv.split(CSV_DELIM)
        return Viatura(
            matricula = attrs[0],
            marca = attrs[1],
            modelo  = attrs[2],
            data = attrs[3],
        )
    #:

    @property
    def ano(self) -> int:
        return self.data.year
    #:

    def  __str__(self) -> str:
        return f"Matricula: {self.matricula} Marca/Modelo: {self.marca}/{self.modelo}"
    #:

    def __repr__(self) -> str:
        return f"Viatura('{self.matricula}', '{self.marca}', '{self.modelo}', '{self.data}')"
    #:
#:

class InvalidProdAttr(ValueError):
    """
    Invalid Product Attribute.
    """
    pass
#:

def valida_matricula(matricula: str) -> bool:
    """
    DD-LL-DD
    """
    partes = matricula.split('-')
    return (
            len(partes) == 3
        and (partes[0].isdigit() and len(partes[0]) == 2)
        and (partes[1].isalpha() and len(partes[1]) == 2 and partes[1] == partes[1].upper())
        and (partes[2].isdigit() and len(partes[2]) == 2)
    )
#:

def valida_marca(marca: str) -> bool:
    """
    Uma ou mais palavras alfanuméricas
    """
    palavras = marca.split()
    return len(palavras) >= 1 and all(palavra.isalnum() for palavra in palavras)
#:

# def valida_marca(marca: str) -> bool:
#     """
#     Uma ou mais palavras alfanuméricas
#     """
#     palavras = marca.split()
#     for palavra in palavras:
#         if not palavra.isalnum():
#             return False
#     return True
# #:

def valida_modelo(modelo):
    return valida_marca(modelo)
#:

################################################################################
##
##       CATÁLOGO DE VIATURAS (VEHICLE COLLECTION)
##
################################################################################

class VehicleCollection:
    def __init__(self):
        self.vehicles = []
    #:

    def append(self, viat: Viatura):
        if self.search_by_id(viat.matricula):
            msg = f'Já existe viatura com matricula {viat.matricula} na colecção'
            raise DuplicateValue(msg)
        self.vehicles.append(viat)
    #:

    def search_by_id(self, matricula: str) -> Viatura | None:
        for viat in self.vehicles:
            if viat.matricula == matricula:
                return viat
        return None
    #:

    def _dump(self):
        for viat in self.vehicles:
            print(f"{viat.marca}/{viat.modelo} matricula: {viat.matricula}")
    #:
#:

class DuplicateValue(Exception):
    pass
#:

################################################################################
##
##       I/O: LEITURA E ESCRITA DA BD DE VIATURAS
##
################################################################################

def read_vehicles(in_file_path: str) -> VehicleCollection:
    vehicles = VehicleCollection()
    with open(in_file_path, 'rt') as in_file:
        for line in relevant_lines(in_file):
            vehicles.append(Viatura.from_csv(line))
    return vehicles
#:

def relevant_lines(file: TextIO):
    for line in file:
        line = line.strip()
        if len(line) == 0:
            continue
        if line.startswith('##') or line.startswith('//'):
            continue
        yield line   # TODO: remover '\n'
#:


################################################################################
##
##       MAIN E MENU PRINCIPAL
##
################################################################################

vehicles: VehicleCollection

def main():
    global produtos
    vehicles = read_vehicles('viaturas.csv')
    vehicles._dump()
#:

if __name__ == '__main__':
    main()
