
path = input("Caminho para o ficheiro: ")

try:
    with open(path, 'rt') as file:
        print(2/0)
        for line in file:
            print(line, end='')
    print("\n\n   --> FICHEIRO LIDO COM SUCESSO!!! <--- \n\n")
except FileNotFoundError as ex:
    print(f"Erro: caminho '{ex.filename}' inválido")
except PermissionError as ex:
    print(f"Erro: Não tem permissões para aceder a '{ex.filename}'")
except IsADirectoryError as ex:
    print(f"Erro: '{ex.filename}' é uma directoria/pasta")
except Exception as ex:
    print(f"Erro: problemas ao abrir {path}")
    print(ex)

print("FIM")

# https://docs.python.org/3/library/exceptions.html
# https://docs.python.org/3/library/exceptions.html#os-exceptions


"""
try:
    BLOCO_DE_CODIGO_PONTENCIALMENTE_COM_ERROS
except Excepcao1/Erro1:
    BLOCO_DE_CODIGO_QUE_TRATA_DA_EXCEPCAO1
except Excepcao2/Erro2:
    BLOCO_DE_CODIGO_QUE_TRATA_DA_EXCEPCAO2
finally:
    BLOCO_EXECUTADO_QUER_TENHA_OCORRIDO_EXCEPÇÃO_OU_NÃO
"""

"""
class A:        # superclasse
    def __init__(self, x):
        self.x = x
    def metodo1(self, y):
        return self.x + y

class B(A):     # subclasses  / classe derivada
    def metodo2(self, y, z):
        return self.x + 2 * y + 3 * z

class C(A):     # subclasses    / classe derivada
    def metodo1(self, y):
        return super().metodo1(y) * 2.5
        # return A.metodo1(self, y) * 2.5
"""

"""
  Exception 
  |
  +----- OSError
  |       |
  |       +---- FileNotFoundError
  |       +---- IsADirectoryError
  |       +---- etc
  +----- ValueEror

class Exception: ...
class OSError(Exception): ....
class FileNotFoundError(OSError): ... 
class FileNotFoundError(IsADirectoryError): ... 
class ValueError(Exception): ...
"""

"""
file = None
try:
    file = open(path, 'rt') 
    for line in file:
        print(line, end='')
except FileNotFoundError as ex:
    print(f"Erro: caminho '{ex.filename}' inválido")
finally:
    if file:
        file.close()
"""