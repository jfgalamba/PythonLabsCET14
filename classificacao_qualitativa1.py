"""
ENUNCIADO
    1. Pedir classificações ao utilizador (devem estar estão entre 0 e 20)
    2. Classificação qualitativa da classificação quantitativa introduzida:
        0-4: Fraco
        5-9: Insuficiente
        10-14: Suficiente
        15-20: Bom
        > 20: Inválida (ou seja, é um erro)  (NOTA < 0: indica que o programa 
                                               deve terminar)
    3. Se classificação for um número negativo, o programa termina

EXEMPLO:
    Insira uma classificação: 12
    Classificação qualitativa "Suficiente"

    Insira uma classificação: 7
    Classificação qualitativa "Insuficiente"

    Insira uma classificação: 17
    Classificação qualitativa "Bom"

    Insira uma classificação: 31
    ATENÇÃO: classificação 31 INVÁLIDA!

    Insira uma classificação: -1
    Fim do programa

"""

def main():
    classif = 0
    while classif >= 0:
        classif = int(input("Insira uma classificação [0-20]: "))
        if 0 <= classif < 5:
            print("Fraco")
        elif 5 <= classif < 10:
            print("Insuficiente")
        elif 10 <= classif < 15:
            print("Suficiente")
        elif 15 <= classif <= 20:
            print("Bom")
        elif classif > 20:
            print(f"Classificação {classif} inválida")

        print("FIM DESTA REPETIÇÃO/ITERAÇÃO")

    print("FIM DO CICLO WHILE")
#:

if __name__ == '__main__':
    main()

# CICLO while

#     while CONDIÇÃO:
#         INST1
#         INST2
#         ...
#         INST_N
