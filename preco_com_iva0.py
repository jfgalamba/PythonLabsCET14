"""
Faca um programa para calcular o preco de venda final de um produto. 
Para tal solicita, através da linha de comandos (shell), o preco do produto, 
o valor da taxa de IVA a aplicar e (opcionalmente) o valor de um desconto a 
aplicar ao valor final do produto. O programa devera dar instrucoes ao 
utilizador de como deve ser invocado. O valor do IVA e do desconto deve 
ser dado em percentagem.

Nesta versão:
    - preço e restantes parâmetros são obtidos a partir da entrada padrão /
      standard input (ie, por via do input)
    - desconto não é opcional
    - também vamos ignorar "O programa deverá dar instruções ao utilizador 
        de como deve ser invocado.
"""

from decimal import Decimal as dec

preco    = dec(input("Preço       : "))
taxa_iva = dec(input("IVA  %      : "))
desconto = dec(input("Desconto %  : "))

preco_final = preco * (1 + taxa_iva/100) * (1 - desconto/100)

print(f"PREÇO FINAL : {preco_final:.2f}")

"""
DEMONSTRAÇÃO DA FÓRMULA:
preco = 200
taxa_iva = 23
desconto = 10

preco_final = 200 * (1 + 23/100) * (1 - 10/100)
            = 200 * 1.23 * 0.9
            = 246 * 0.9
            = 221.4
"""