# - Exercício: script (calculos2.py) que pede número (float) ao utilizador e 
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
#  v2: testar c/ 10.3 incorporar decimal


from decimal import Decimal as dec

num = dec(input("Introduza um número: "))

print("Dobro     :", 2 * num)
print("Triplo    :", 3 * num)
print("Quadrado  :", num ** 2)
print("Cubo      :", num ** 3)
print("2.5x + 10 :", dec('2.5') * num + 10)
