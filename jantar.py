"""
Um grupo de pessoas participou num jantar em que todos encomendaram o 
menu turístico e pretende fazer um programa para calcular a conta. 
Para tal, o programa deve comecar por ler o número de pessoas 
envolvidas no jantar e, de seguida, calcular o valor da conta. O menu 
custa 15,00 € + IVA por pessoa. Assuma que o IVA é 23% e a gorjeta 
para o empregado é de 10% sobre o montante total com IVA. O programa 
deve exibir a despesa total sem IVA e sem gorjeta, o montante de IVA, o
valor da gorjeta e a despesa total final.
"""

from decimal import Decimal as dec

preco_menu = dec('15')      # preço p/ pessoa em €
taxa_iva   = dec('0.23')    # taxa de IVA em %
gorjeta    = dec('0.10')    # 10% de gorjeta

num_pessoas = int(input("Jantar para quantas pessoas? "))

despesa_s_iva    = num_pessoas * preco_menu
montante_iva     = despesa_s_iva * taxa_iva
despesa_c_iva    = despesa_s_iva + montante_iva
montante_gorjeta =  despesa_c_iva * gorjeta

total = despesa_c_iva + montante_gorjeta

print(f"Despesa s/ IVA : {despesa_s_iva:8.2f} €")
print(f"Montante IVA   : {montante_iva:8.2f} €")
print(f"Despesa c/ IVA : {despesa_c_iva:8.2f} €")
print(f"Gorjeta (10%)  : {montante_gorjeta:8.2f} €")
print()
print(f"Despesa TOTAL  : {total:8.2f} €")
