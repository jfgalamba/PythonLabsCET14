"""
Faca um programa para calcular o preco de venda final de um produto. 
Para tal solicita, através da linha de comandos (shell), o preco do produto, 
o valor da taxa de IVA a aplicar e (opcionalmente) o valor de um desconto a 
aplicar ao valor final do produto. O programa devera dar instrucoes ao 
utilizador de como deve ser invocado. O valor do IVA e do desconto deve 
ser dado em percentagem.

Nesta 4a versão:
    - desconto passa a ser opcional
    - utilizamos a expressão IF
"""

import sys
from decimal import Decimal as dec

if len(sys.argv) not in (3, 4):
    print(f"Utilização: {sys.argv[0]} PREÇO TAXA_IVA [DESCONTO%]", file=sys.stderr)
    sys.exit(2)

preco    = dec(sys.argv[1])
taxa_iva = dec(sys.argv[2])
desconto = dec( sys.argv[3] if len(sys.argv) == 4 else '0'  )

preco_final = preco * (1 + taxa_iva/100) * (1 - desconto/100)

print(f"PREÇO FINAL : {preco_final:.2f}")


"""
x = 15
txt = 'codigo1' if x > 10 else 'codigo2'
# Em linguagens derivadas de C: x > 10 ? 'codigo1' : 'codigo2'

if x > 10:
    txt = 'codigo1'
else:
    txt = 'codigo2'

# Expressão IF / Expressão Condicional
#
#       CONSEQUÊNCIA if CONDIÇÃO else ALTERNATIVA
#
# Operador Ternário (linguagens derivadas de C):
#
#       CONDIÇÃO ? CONSEQUÊNCIA : ALTERNATIVA

"""