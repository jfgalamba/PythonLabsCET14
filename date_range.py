"""
Defina um gerador para datas semelhante em "espírito" ao range. Ou seja, 
pode receber um, dois ou três argumentos. Se receber apenas um argumento,
gera todas as datas da data actual até essa data. Se receber dois 
argumentos, assume que esses argumentos são datas e gera todas as datas 
entre as datas passadas como argumento. O terceiro argumento, caso seja 
utilizado, é um número inteiro que indica o número de dias de intervalo 
entre as datas a gerar. Dê o nome `date_range` ao gerador.
"""
from datetime import date, timedelta

def date_range(first: date, last: date | None = None, step = 1):
    if last is None:
        last = first
        first = date.today()
    days = (last - first).days
    for i in range(0, days, step):
        yield first + timedelta(days=i)
#:

def test():
    for dt in date_range(date(2024, 2, 27), date(2024, 3, 3)):
        print(dt)
    """
    2024-02-27
    2024-02-28
    2024-02-29
    2024-03-01
    2024-03-02
    """
#:
