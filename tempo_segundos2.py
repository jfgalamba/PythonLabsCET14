"""
Desenvolva um programa a solicitar a entrada de horas, minutos e segundos, 
calculando depois o tempo total em segundos.
Nesta versão a informação é introduzida na linha de comandos quando se 
executa o programa
"""

import sys

horas = int(sys.argv[1])
mins  = int(sys.argv[2])
segs  = int(sys.argv[3])

print(f"Tempo total em segundos: {horas * 3600 + mins * 60 + segs}")
