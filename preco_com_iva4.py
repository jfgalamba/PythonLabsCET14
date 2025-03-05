"""
Faca um programa para calcular o preco de venda final de um produto. 
Para tal solicita, através da linha de comandos (shell), o preco do produto, 
o valor da taxa de IVA a aplicar e (opcionalmente) o valor de um desconto a 
aplicar ao valor final do produto. O programa devera dar instrucoes ao 
utilizador de como deve ser invocado. O valor do IVA e do desconto deve 
ser dado em percentagem.

Nesta 4a versão:
    - desconto passa a ser opcional
"""

import sys
from decimal import Decimal as dec

# if len(sys.argv) != 3 and len(sys.argv) != 4:
if len(sys.argv) not in (3, 4):
    print(f"Utilização: {sys.argv[0]} PREÇO TAXA_IVA [DESCONTO%]", file=sys.stderr)
    sys.exit(2)

# só chegamos aqui se len(sys.argv) == 4 (caso contrário, o sys.exit teria
# sido executado e o programa teria terminado com código de erro 2)
preco    = dec(sys.argv[1])
taxa_iva = dec(sys.argv[2])
if len(sys.argv) == 4:
    desconto = dec(sys.argv[3])
else:
    desconto = dec('0')

preco_final = preco * (1 + taxa_iva/100) * (1 - desconto/100)

print(f"PREÇO FINAL : {preco_final:.2f}")


"""
x = ...

# if x == 78 or x == 99 or x == 157:
if x in (78, 99, 157):
    print("dadsada")
    print("1312")
    x *= 2

y = ...
# if y != 44 and y != 153 and y != 207 and y != 959:
if y not in (44, 153, 207, 959)
    y /= 2
    z = y + 90

"""