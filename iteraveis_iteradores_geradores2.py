# ITERÁVEL: Objecto a partir do qual tiramos um iterador
#           Na prática, um iterável é um objecto que pode 
#           estar à direita de um ciclo FOR.
#           Se um objecto é iterável em Python, então 
#           conseguimos obter um iterador através da função
#           ITER.
#
# ITERADOR: Objecto que permite obter o próximo elemento de
#           um iterável. Um iterador é também um iterável.
#           Dado um iterador, acedemos ao próximo elemento 
#           (e fazemos avançar o iterador) através da função 
#           NEXT.
#
# GERADOR:  Um objecto criado a partir de uma função (geradora) que pode 
#           ser parada ("pause") e retomada a partir do ponto onde 
#           ficou. Ou seja, um gerador tem "memória". Um gerador 
#           é também um iterador.
#           Qualquer função com a palavra-reservada YIELD é 
#           uma função geradora (ie, que devolve um gerador).
#
#       ITERÁVEL
#          ^
#          |
#       ITERADOR
#          ^
#          |
#       GERADOR

from typing import Iterable

nome = 'alberto'                                                # str
nums = (10, 21, 3, 87, -10, 18, 17, 301, -450, 28, 8, 5, 4)     # tuple
idades = {'ana': 23, 'bruno': 40, 'carlos': 15}                 # dict

for x in nome:
    print(x)

for x in nums:
    print(x)

for x in idades:
    print(x)

# def mapeia(itens: Iterable, fun) -> list:
#     itens2 = []
#     for item in itens:
#         itens2.append(fun(item))
#     return itens2
# #:

# def filtra(itens: Iterable, criterio) -> list:
#     seleccionados = []
#     for item in itens:
#         if criterio(item):
#             seleccionados.append(item)
#     return seleccionados
# #:

def mapeia(itens: Iterable, fun):
    for item in itens:
        yield fun(item)
#:

def filtra(itens: Iterable, criterio):
    for item in itens:
        if criterio(item):
            yield item
#:

nums = (10, 21, 3, 87, -10, 18, 17, 301, -450, 28, 8, 5, 4)  # 10.000.000 elementos
#...
nums3 = mapeia(nums, lambda x: x * 3)   # TOTAL: 20.000.000 em memória
#...
pares = filtra(nums3, lambda x: x % 2 == 0)  # 50% pares 10.000.000 
                                             # TOTAL: 30.000.000
#...
pares_positivos = filtra(pares, lambda x: x > 0)  # 50% positivos 5.000.000
                                                  # TOTAL: 35.000.000
#...
pares_positivos_entre_0_e_100 = filtra(pares_positivos, lambda x: 0 < x < 100)
                                                  # 99% ~ 5.000.000
                                                  # TOTAL: aprox. 40.000.000
sum(pares_positivos_entre_0_e_100)