"""
Desenvolva um programa a solicitar a entrada de horas, minutos e segundos, 
calculando depois o tempo total em segundos.
"""

horas = int(input("Horas? "))
mins  = int(input("Minutos? "))
segs  = int(input("Segundos? "))

print(f"Tempo total em segundos: {horas * 3600 + mins * 60 + segs}")
