"""
Conversor cambial EUR<->USD. 
Exibe um menu com as opções em baixo indicadas.

    $ python3 conversor_cambial1.py

    Escolha o sentido da conversao
    1. Euros -> Dólares
    2. Dólares -> Euros
    > 2

    Montante em dólares: 2000
    Euros -> 1851.85

    Pretende efectuar mais conversões (S/N)? s

    Escolha o sentido da conversao
    1. Euros -> Dolares
    2. Dólares -> Euros
    > 1

    etc.

    Pretende efectuar mais conversões (S/N)? x
    ERRO: opção <x> é inválida.
    Pretende efectuar mais conversões (S/N)? n
    Fim do programa

    $ 

NOTAS:
    1. Nesta versão o câmbio é fixo 
    2. Programa pergunta ao utilizador se deseja repetir
    3. Função confirma
"""

from decimal import Decimal as dec


def main():
    cambio = dec('1.087')       # EURUSD à data de 05/11/2024
    while True:
        # 1. Exibir o menu
        print("Escolha o sentido da conversao")
        print("1. Euros -> Dólares")
        print("2. Dólares -> Euros")

        # 2. Pedir opção utilizador
        opcao = input("> ")

        # 3. Analisar e executar a opção indicada
        match opcao.upper():
            case '1':
                euros = dec(input("Montante em euros: "))
                dolares = euros * cambio
                print(f"Dólares -> {dolares:.2f}")
            case '2':
                dolares = dec(input("Montante em dólares: "))
                euros = dolares / cambio
                print(f"Euros -> {euros:.2f}")
            case _:
                print(f"Opção <{opcao}> inválida")

        # 4. Repetir ou sair do programa
        if not confirma("Pretende efectuar mais conversões (S/N)? "):
            print("Fim do programa")
            break
#:

def confirma(pergunta: str) -> bool:
    while True:
        resposta = input(pergunta)
        match resposta.upper():
            case 'S' | 'SIM':
                return True
            case 'N' | 'NAO' | 'NÃO':
                return False
            case _:
                print(f"ERRO: opção <{resposta}> é inválida.")
#:

if __name__ == '__main__':
    main()
