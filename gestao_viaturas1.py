"""
Programa para gestão do catálogo/stand de viaturas. Este programa irá 
suportar operações como as em baixo indicadas:
    - Listar o catálogo
    - Pesquisar por alguns campos 
    - Eliminar um registo do catálogo
    - Guardar o catálogo em ficheiro

v1: a) Definição e utilização de uma viatura
"""

from datetime import date

class Vehicle:
    def __init__(
            self,
            license_plate: str,       # matrícula
            make: str,
            model: str,
            date_: str,
    ):
        # 1. Validar os parâmetros do construtor
        # 2. Inicializar e definir o objecto
        self.license_plate = license_plate
        self.make = make
        self.model = model
        self.date = date.fromisoformat(date_)
    #:
#:

def main():
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

    print(f"VIATURA: {v1.license_plate} {v1.make}/{v1.model}")
    print(f"VIATURA: {v2.license_plate} {v2.make}/{v2.model}")
#:

if __name__ == '__main__':
    main()
