# - Exercício: script (calculos3.py) que pede número (float) ao utilizador e 
#   que exibe:
#     . dobro
#     . triplo
#     . quadrado
#     . cubo
#     . resultado de 2.5x + 10, onde x é o número pedido ao utilizador
#
#   $ python calculos1.py
#   Introduza um número: 3
#   Dobro     : 6.0
#   Triplo    : 9.0
#   Quadrado  : 9.0
#   Cubo      : 27.0
#   2.5x + 10 : 17.5
#   $ 
#
#  v3: format / f-strings

from decimal import Decimal as dec

num = dec(input("Introduza um número: "))

print(f"Dobro     : {2 * num:8.2f}")
print(f"Triplo    : {3 * num:8.2f}")
print(f"Quadrado  : {num ** 2:8.2f}")
print(f"Cubo      : {num ** 3:8.2f}")
print(f"2.5x + 10 : {dec('2.5') * num + 10:8.2f}")
