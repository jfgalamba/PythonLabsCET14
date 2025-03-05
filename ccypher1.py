#!/usr/bin/env python3
"""
O algoritmo de César é um algoritmo de encriptação que aplica um deslocamento
fixo a todos os bytes de um ficheiro de entrada. Neste algoritmo, cada byte
da entrada é substituido por um outro byte N posições à frente, sendo este 
N fixo para todos os bytes. N é designado por deslocamento ou shift.

    $ ccypher.py -e [-s SHIFT] FILE
    $ ccypher.py -d -s SHIFT FILE
    $ ccypher.py --decrypt --shift=SHIFT FILE

Deslocamento = 7
Entrada : b'\x0b\x13\x01\xfd'
    \x0b = 11  -> \x12 = 18
    \x13 = 19  -> \x1a = 26 
    \x01 = 1   -> \x08 = 8 
    \xfd = 253 -> \x04 = 4

Saída  : b'\x12\x1a\x08\x04'
"""

def encrypt(in_path: str, out_path: str, shift: int):
    with open(in_path, 'rb') as in_file:
        with open(out_path, 'wb') as out_file:
            while next_byte := in_file.read(1):
                next_byte_int = next_byte[0]
                out_byte_int = (next_byte_int + shift) % 256
                out_file.write(bytes([out_byte_int]))
#:

def decrypt(in_path: str, out_path: str, shift: int):
    with open(in_path, 'rb') as in_file:
        with open(out_path, 'wb') as out_file:
            while next_byte := in_file.read(1):
                next_byte_int = next_byte[0]
                out_byte_int = (next_byte_int - shift) % 256
                out_file.write(bytes([out_byte_int]))
#:

def main():
    import sys
    import argparse

    parser = argparse.ArgumentParser(
        description="ccypher: Cifra de César"
    )
    parser.add_argument(
        'FILE',
        help = 'Decrypt file',
    )
    parser.add_argument(
        '-s', '--shift',
        type=int,
        required=True,
    )
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument(
        '-e', '--encrypt',
        action = 'store_true',
        help = 'Encrypt file',
    )
    group.add_argument(
        '-d', '--decrypt',
        action = 'store_true',
        help = 'Decrypt file',
    )
    args = parser.parse_args()

    if args.encrypt:
        # convém verificar se ficheiro de saida existe antes de escrever por cima
        out_path = f'{args.FILE}.ccy'
        encrypt(args.FILE, out_path, args.shift)
    elif args.decrypt:
        # convém verificar se ficheiro de saida existe antes de escrever por cima
        if not args.FILE.endswith('.ccy'):
            print("File doesn't have required '.ccy' extension.", file=sys.stderr)
            sys.exit(2)
        out_path = args.FILE[:-4]
        if not out_path:
            print("File name is empty.", file=sys.stderr)
            sys.exit(2)
        decrypt(args.FILE, out_path, args.shift)
#:

if __name__ == '__main__':
    main()

"""
with open(in_path, 'rb') as in_file:
    with open(out_path, 'wb') as out_file:
        pass

with ( 
    open(in_path, 'rb') as in_file, 
    open(out_path, 'wb') as out_file
):
    pass

"""