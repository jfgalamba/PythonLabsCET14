#
# for ELEM in COLECÇÃO:
#     INST1
#     INST2
#     ...
#     INST_N
#
# ELEM é uma variável

# 1o EXEMPLO: Ciclo de contagem (gama de valores)
print("1o EXEMPLO: Ciclo de contagem (gama de valores)")

soma = 0
for i in range(1, 6):
    soma += i
print(f"Soma: {soma}")
print(f"Último valor de i: {i}")


# 2o EXEMPLO: Percorrer os elementos de uma estrutura de dados (string)
print("2o EXEMPLO: Percorrer os elementos de uma estrutura de dados (string)")
nome = 'ALBERTO'

for letra in nome:
    print(letra)

print('-----------')

for i, letra in enumerate(nome):
    print(f"{i} -> {letra}")

print('-----------')

for letra in reversed(nome):
    print(letra)

# 3o EXEMPLO: Percorrer os elementos de uma estrutura de dados (lista)
print("3o EXEMPLO: Percorrer os elementos de uma estrutura de dados (lista)")
vals = [10, -50, 40, -29]

soma = 0
for val in vals:
    soma += val
print(f"Soma: {soma}")

# 4o EXEMPLO: Dicionários
print("5o EXEMPLO: Dicionários")
idades = {'alberto': 23, 'ana': 55, 'armando': 19, 'arnaldo': 47}

for nome in idades:
    print(nome)

for nome in idades:
    print(f"Idade do {nome} é {idades[nome]}")

for nome, idade in idades.items():
    print(f"Idade do {nome} é {idade}")

for idade in idades.values():
    print(idade)
