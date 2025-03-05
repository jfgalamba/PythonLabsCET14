#!/usr/bin/env python3
"""
Pretende fazer um programa em Python para gerar aleatoriamente grupos
de alunos para a realização de projectos e trabalhos de grupo. O seu
script deve processar um ficheiro de entrada com os nomes dos alunos,
um por linha, e gerar um ficheiro de saída para onde deve enviar a 
listagem dos grupos, um grupo por linha com os nomes separados por
vírgulas. Deve também receber o número de elementos a agrupar.

O script deve ser invocado de acordo a com a seguinte sintaxe: 
    $ agrupa.py [-i FICHEIRO_ENTRADA] [-o FICHEIRO_SAÍDA] [-n NUM]

    FICHEIRO_ENTRADA : valor por omissão -> sys.stdin
    FICHEIRO_SAÍDA   : valor por omissão -> sys.stdout
    NUM              : valor por omissão -> 2
    A ordem das opções não é fixa

    $ agrupa.py -i nomes_completos.txt -o grupos.txt -n 3
    $ agrupa.py -o grupos.txt -i nomes_completos.txt -n 3
    $ agrupa.py -n 3 -o grupos.txt -i nomes_completos.txt

    # lê linhas de nomes_completos.txt e exibe os grupos na saída padrão
    $ agrupa.py -i nomes_completos.txt -n 3
    $ agrupa.py --input-file=nomes_completos.txt --group-size=3

    # lê as linhas introduzidos pelo utilizador (entrada padrão) e envia
    # os grupos para ficheiro grupos.txt
    $ agrupa.py -o grupos.txt -n 3
    $ agrupa.py --output-file=grupos.txt -n 3

    NOTA: Esta versão utiliza a biblioteca argparse (não é preciso instalar 
    pq faz parte da biblioteca padrão do Python)

(c) 2024 Alberto Antunes, Armando Almeida

Código fonte de acordo com a licença GPL3. Deverá consultar:
    https://www.gnu.org/licenses/gpl-3.0.en.html
"""

from random import shuffle

def group_elements(elements: list, group_size: int) -> list[list]:
    """
    Devolve uma lista grupos aleatórios de elementos da lista `elements`.
    A dimensão dos grupos é dada por `group_size`.
    Exemplos
        L1 = [10, 20, 30, 40, 50]
        L2 = group_elements(L1, 2)
        L2 => [[30, 10], [20, 50], [40]]

        L1 = [10, 20, 30, 40, 50, 60, 70, 80]
        L2 = group_elements(L1, 3)
        L2 => [[40, 10, 50], [30, 20, 70], [80, 60]]

        L1 = ['ola mundo', 'adeus mundo', 'buffer overflow', 'gpl3 é fixe', 
              'está a chover']
        L2 = group_elements(L1, 2)
        L2 = [['adeus mundo', 'buffer overflow'], ['gpl3 é fixe', 'adeus mundo'],...]
    """
    shuffle(elements)
    groups = []
    for i in range(0, len(elements), group_size):
        groups.append(elements[i:i + group_size])
    return groups
#:

def main():
    import sys
    from docopt import docopt

    doc = f"""
Groups lines from the input given by INPUT FILE. 

Usage:
    {sys.argv[0]} [-i INPUT_FILE] [-o OUTPUT_FILE] [-n NUM]

Options:
    -i INPUT_FILE, --input=INPUT_FILE      Path to input file
    -o OUTPUT_FILE, --output=OUTPUT_FILE   Path to output file
    -n NUM, --group-size=NUM               Group size [default: 2]
"""     
    args = docopt(doc)

    lines = []
    file = open(args['--input'], 'rt') if args['--input'] else sys.stdin
    with file:
        for line in file:
            line = line.strip()
            if len(line) > 0:
                lines.append(line)

    groups = group_elements(lines, int(args['--group-size']))

    file = open(args['--output'], 'rt') if args['--output'] else sys.stdout
    with file:
        for group in groups:
            line = ', '.join(group)
            print(line, file=file)
#:

if __name__ == '__main__':
    main()


# https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
# https://docs.python.org/3/library/functions.html#open
# https://docs.python.org/3/library/io.html#
# https://docs.python.org/3/tutorial/stdlib.html#command-line-arguments
# https://docs.python.org/3/howto/argparse.html#argparse-tutorial
# https://docs.python.org/3/library/argparse.html#module-argparse

