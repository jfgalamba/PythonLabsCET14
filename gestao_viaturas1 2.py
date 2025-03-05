"""
Programa para gestão de um catálogo/stand de viaturas. Este programa 
permitirá:
    - Listar o catálogo
    - Pesquisar por alguns campos 
    - Eliminar um registo do catálogo
    - Guardar o catálogo em ficheiro

v1: a) Definição e utilização de uma viatura
"""

# # matricula (str), marca, modelo, data
# 10-XY-20,Opel,Corsa XL,2019-10-15
# 20-PQ-15,Mercedes,300SL,2017-05-31

from datetime import date

class Viatura:
    def __init__(
            self,
            matricula: str,
            marca: str,
            modelo: str,
            data: str,      # OU data: date
    ):
        # 1. Validar parâmetros (já lá vamos...)
        # 2. Associar parâmetros a atributos/campos
        self.matricula = matricula
        self.marca = marca
        self.modelo = modelo
        self.data = date.fromisoformat(data)
        # self.data = data
    #:
#:

def main():
    viat1 = Viatura(
        matricula = '10-XY-20',
        marca = 'Opel',
        modelo = 'Corsa XL',
        data = '2019-10-15',
        # data = date(2019, 10, 15),
    )

    viat2 = Viatura(
        matricula = '20-PQ-15',
        marca = 'Mercedes',
        modelo = '300SL',
        data = '2017-05-31',
    )

    print(f"VIATURA: {viat1.matricula} {viat1.marca}/{viat1.modelo}")
    print(f"VIATURA: {viat2.matricula} {viat2.marca}/{viat2.modelo}")
#:

if __name__ == '__main__':
    main()