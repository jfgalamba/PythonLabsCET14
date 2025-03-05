"""
Pretende-se calcular a idade em anos em funcao do dia, mês e ano de 
nascimento e dia, mês e ano atual. Tenha em atencao o seguinte: em 
condições normais a idade é a diferenca entre o ano atual e ano de
nascimento, porém, se o mês actual for inferior ao mês de nascimento
ou o mês atual igual ao mês de nascimento e o dia atual inferior ao
dia de nascimento a idade é o ano atual menos o ano de nascimento
menos um.

Esta versão é interactiva: a data de nascimento é pedida ao utilizador 
(via input)

ENTRADA:
YYYY MM DD introduzidos numa linha de texto (ie, numa string)
"""

from datetime import date


def main():
    date_parts = input("Indique a sua data de nascimento (YYYY MM DD): ").split()
    ano_nasc = int(date_parts[0])
    mes_nasc = int(date_parts[1])
    dia_nasc = int(date_parts[2])

    hoje = date.today()
    idade = hoje.year - ano_nasc
    if hoje.month < mes_nasc or hoje.month == mes_nasc and hoje.day < dia_nasc:
        idade -= 1
    print(f"A sua idade é {idade} anos")
#:

if __name__ == '__main__':
    main()
