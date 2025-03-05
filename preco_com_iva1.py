"""
Faca um programa para calcular o preco de venda final de um produto. 
Para tal solicita, através da linha de comandos (shell), o preco do produto, 
o valor da taxa de IVA a aplicar e (opcionalmente) o valor de um desconto a 
aplicar ao valor final do produto. O programa devera dar instrucoes ao 
utilizador de como deve ser invocado. O valor do IVA e do desconto deve 
ser dado em percentagem.

Nesta 1a versão:
    - desconto não é opcional
    - também vamos ignorar "O programa deverá dar instruções ao utilizador 
        de como deve ser invocado.
"""

import sys
from decimal import Decimal as dec

preco    = dec(sys.argv[1])
taxa_iva = dec(sys.argv[2])
desconto = dec(sys.argv[3])

preco_final = preco * (1 + taxa_iva/100) * (1 - desconto/100)

print(f"PREÇO FINAL : {preco_final:.2f}")

