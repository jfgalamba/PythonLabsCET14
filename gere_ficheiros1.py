import os
import shutil

def main():
    print("COMANDOS PARA GESTÃO DE FICHEIROS")
    cmd_args  = input(">> ")

    match cmd_args.split():
        case ['ajuda']:
            print("\nComandos disponíveis:")
            print("  apaga fich")
            print("  dup fich")
            print("  move fich destino\n")

        case ['apaga' | 'APAGA', fich]:
            resp = input(f"Pretende apagar o ficheiro {fich} (S/N)? ")
            if resp in ('S', 's'):
                os.remove(fich)
                print(f"Ficheiro {fich} removido")

        case ['apagadir' | 'APAGADIR', dir_]:
            resp = input(f"Pretende apagar a directoria {dir_} (S/N)? ")
            if resp in ('S', 's'):
                shutil.rmtree(dir_)
                print(f"Directoria {dir_} removida")

        case ['dup' | 'DUP', fich]:
            dup_fich = f'{fich}.dup'
            shutil.copy(fich, dup_fich)
            print(f"Criada cópia de {fich} em {dup_fich}")

        case ['move' | 'MOVE', fich, destino]:
            resp = input(f"Pretende mover o ficheiro {fich} para {destino} (S/N)? ")
            if resp in ('S', 's'):
                shutil.move(fich, destino)
                print(f"Ficheiro {fich} movido para {destino}")

        case ['ren' | 'REN', fich, novo_nome]:
            resp = input(f"Pretende renomear o ficheiro {fich} para {novo_nome} (S/N)? ")
            if resp in ('S', 's'):
                shutil.move(fich, novo_nome)
                print(f"Ficheiro {fich} renomeado para {novo_nome}")

        case _:
            print(f"ERRO: Sintaxe inválida:\n\t{cmd_args}")


if __name__ == '__main__':
    main()
