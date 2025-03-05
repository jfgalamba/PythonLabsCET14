"""
Pretende-se calcular a idade em anos em funcao do dia, mês e ano de 
nascimento e dia, mês e ano atual. Tenha em atencao o seguinte: em 
condições normais a idade é a diferenca entre o ano atual e ano de
nascimento, porém, se o mês actual for inferior ao mês de nascimento
ou o mês atual igual ao mês de nascimento e o dia atual inferior ao
dia de nascimento a idade é o ano atual menos o ano de nascimento
menos um.

Esta versão é não-interactiva: a data de nascimento é introduzida 
através da linha de comandos.

ENTRADA:
YYYY MM DD introduzidos na linha de comandos
"""

import sys
from datetime import date

def main():
    if len(sys.argv) != 4:
        print(f"Utilização: {sys.argv[0]} YYYY MM DD", file=sys.stderr)
        sys.exit(2)

    ano_nasc = int(sys.argv[1])
    mes_nasc = int(sys.argv[2])
    dia_nasc = int(sys.argv[3])

    hoje = date.today()
    idade = hoje.year - ano_nasc
    if hoje.month < mes_nasc or hoje.month == mes_nasc and hoje.day < dia_nasc:
        idade -= 1
    print(f"A sua idade é {idade} anos")

if __name__ == '__main__':
    main()
