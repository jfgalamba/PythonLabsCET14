"""
Conversor cambial EUR<->USD. 
Exibe um menu com as opções em baixo indicadas.

    $ python3 conversor_cambial1.py

    Escolha o sentido da conversao
    1. Euros -> Dólares
    2. Dólares -> Euros
    T. Terminar
    > 2

    Montante em dólares: 2000
    Euros -> 1851.85

    Escolha o sentido da conversao
    1. Euros -> Dolares
    2. Dólares -> Euros
    T. Terminar
    > T

    $ 

NOTAS:
    1. Nesta versão o câmbio é fixo 
    2. Menu tem opção extra para terminar o programa
"""

from decimal import Decimal as dec


def main():
    cambio = dec('1.087')       # EURUSD à data de 05/11/2024
    opcao = ''
    while opcao not in ('T', 'TERMINAR'):
        # 1. Exibir o menu
        print("Escolha o sentido da conversao")
        print("1. Euros -> Dólares")
        print("2. Dólares -> Euros")
        print("T. Terminar")

        # 2. Pedir opção utilizador
        opcao = input("> ").upper()

        # 3. Analisar e executar a opção indicada
        match opcao:
            case '1':
                euros = dec(input("Montante em euros: "))
                dolares = euros * cambio
                print(f"Dólares -> {dolares:.2f}")
            case '2':
                dolares = dec(input("Montante em dólares: "))
                euros = dolares / cambio
                print(f"Euros -> {euros:.2f}")
            case 'T' | 'TERMINAR':
                print("Fim do programa")
            case _:
                print(f"Opção <{opcao}> inválida")

if __name__ == '__main__':
    main()
