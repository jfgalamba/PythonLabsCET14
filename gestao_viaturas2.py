"""
Programa para gestão do catálogo/stand de viaturas. Este programa irá 
suportar operações como as em baixo indicadas:
    - Listar o catálogo
    - Pesquisar por alguns campos 
    - Eliminar um registo do catálogo
    - Guardar o catálogo em ficheiro

v2: a) Definir o método display_info
    b) Validar parâmetros c/ excepções
"""

import re
from datetime import date


class Vehicle:
    def __init__(
            self,
            license_plate: str,       # matricula: DD-LL-DD onde D: Dígito L: Letra
            make: str,                # deve ter uma ou mais palavras (apenas letras ou dígitos)
            model: str,               # mesmo que a marca
            date_: str,               # deve vir no formato ISO: 'YYYY-MM-DD'
    ):
        # 1. Validar os parâmetros do construtor
        if not self.validate_license_plate(license_plate):
            raise InvalidAttrValue(f'Matrícula inválida: {license_plate}')

        if not self.validate_make(make):
             raise InvalidAttrValue(f'Marca inválida: {make}')

        if not self.validate_model(model):
             raise InvalidAttrValue(f'Modelo inválido: {model}')

        # 2. Inicializar e definir o objecto
        self.license_plate = license_plate
        self.make = make
        self.model = model
        try:
            self.date = date.fromisoformat(date_)
        except ValueError:
            raise InvalidAttrValue(f"Data inválida: {date_}")
    #:

    def display_info(self):
        print(f"Viatura: '{self.license_plate}' {self.make}/{self.model} {self.date}")
    #:

    def validate_license_plate(self, license_plate: str) -> bool:
        return bool(re.fullmatch(r'[0-9]{2}-[A-Z]{2}-[0-9]{2}', license_plate))
    #:

    def validate_make(self, make: str) -> bool:
        """
        Uma ou mais palavras alfanuméricas
        """
        words = make.split()
        return len(words) >= 1 and all(word.isalnum() for word in words)
    #:

    def validate_model(self, model: str) -> bool:
        return self.validate_make(model)
    #:

    # def validate_license_plate(self, license_plate: str) -> bool:
    #     """
    #     DD-LL-DD
    #     """
    #     parts = license_plate.split('-')
    #     return (
    #             len(parts) == 3
    #         and ( len(parts[0]) == 2 and parts[0].isdigit() )
    #         and ( len(parts[1]) == 2 and parts[1].isalpha() and parts[1] == parts[1].upper() )
    #         and ( len(parts[2]) == 2 and parts[2].isdigit() )
    #     )
    # #:

    # def validate_license_plate(self, license_plate: str) -> bool:
    #     """
    #     DD-LL-DD
    #     """
    #     parts = license_plate.split('-')
    #     if len(parts) != 3:
    #         return False
    #     if len(parts[0]) != 2 or not parts[0].isdigit(): 
    #         return False
    #     if len(parts[1]) != 2 or not parts[1].isalpha() or not parts[1] == parts[1].upper(): 
    #         return False
    #     if len(parts[2]) != 2 or not parts[2].isdigit(): 
    #         return False
    #     return True
    # #:
#:

class InvalidAttrValue(ValueError):
    """
    Valor para atributo inválido
    """

def main():
    try:
        # 10-XY-20|Opel|Corsa XL|2019-10-15
        v1 = Vehicle(
            license_plate = '10-XY-20',
            make = 'Opel',
            model = 'Corsa XL',
            date_ = '2019-10-15',
        )

        # 20-PQ-15|Mercedes|300SL|2017-05-31
        v2 = Vehicle(
            license_plate = '20-PQ-15',
            make = 'Mercedes',
            model = '300SL',
            date_ = '2017-05-31',
        )

        v1.display_info()
        v2.display_info()
    except ValueError as ex:
        print("Problemas ao criar produto:")
        print(ex)
#:

if __name__ == '__main__':
    main()
