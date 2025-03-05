import time

# classe Date
#   + construtores:
#       o __init__ : ano, mes, dia, tem que ser validados (não aceitar 31/4,
#                    29/2/2019, ); lançar excepção do tipo InvalidDateValues que 
#                    deve derivar de ValueError
#                    Não aceitar datas inferiores a 1900
#       o construtor (from_iso): data no formato AAAA-MM-DD
#       o construtor (from_julian): data como inteiro (juliano) AAAAMMDD
#       o construtor (today): devolve data actual
#   + acessores:
#       o year, month, day (properties)
#   + predicados ("acessor" booleano):
#       o is_leap_year
#   + __str__ : mostra data 'AAAA-MM-DD'
#   + __repr__: mostra 'Date(ano, mês, dia)'
#   + outros métodos:
#       o __add__  : nova data igual a data + dias (int)
#       o __radd__ : nova data igual a dias (int) + data
#       o __sub__  : dias (int) que resultam de data - data
#       o __eq__   : verifica se duas datas são iguais
#       * NOTA: usar módulo time para fazer as contas com datas

# import time
#
# t0, s0 = time.time(), time.localtime()
#
# VER: https://docs.python.org/3/library/time.html


class InvalidDateValues(ValueError):
    pass
#:

def test():
    dt0 = Date(2025, 3, 15)
    dt1 = Date(2024, 2, 27)
    print(f'{dt1.year = }')     # 2024
    print(f'{dt1.month = }')    # 2
    print(f'{dt1.day = }')      # 27
    print(f'{dt1.is_leap_year = }')  # True
    print(dt1)                 # 2024-02-27

    iso_date = '2024-02-27'
    dt2 = Date.from_iso('2024-02-27')
    print(f'iso_date {iso_date} => Date {dt2}')
    print(f'dt1 == dt0? {dt1 == dt0}')          # True
    print(f'dt1 == dt2? {dt1 == dt2}')          # True

    julian_date = 20240227
    print(f'julian_date {julian_date} => Date {Date.from_julian(julian_date)}')

    print(f'{dt1} + 2 = {dt1 + 2}')
    print(f'{dt1} - 2 = {dt1 - 2}')

    dt4 = Date(2024, 3, 3)
    print(f'{dt4} - {dt1} = {dt4 - dt1}')    # 5 
    print(f'{dt1} - {dt4} = {dt1 - dt4}')    # -5 

    print(f'Today is {Date.today()!r}')
#:

