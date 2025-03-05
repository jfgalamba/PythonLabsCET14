"""
Determina se um ano introduzido pelo utilizador é um ano
bissexto.

DADOS DE ENTRADA:
    ano: int, >= 0

DADOS DE SAÍDA
    o ano é bissexto? : bool

    e_bissexto = multiplo de 400 ou multiplo de 4 e nao_multiplo de 100
"""

import sys

def main():
    ano = int(input("Indique o ano: "))
    if ano < 0:
        print(f"Ano {ano} inválido")
        sys.exit(1)

    if ano % 400 == 0 or (ano % 4 == 0 and ano % 100 != 0):
        print(f"O ano {ano} é bissexto")
    else:
        print(f"O ano {ano} não é bissexto")

if __name__ == '__main__':      # verifica se o script foi executado
    main()                      # e não foi importado
