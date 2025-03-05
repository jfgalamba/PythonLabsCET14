# Script em Python: ficheiro de código com instruções para serem 
# interpretadas pelo "python3", pela ordem pela qual foram introduzidas
# (isto nem sempre é verdade, mas por agora vamos assumir que sim...)
#
# Um script termina quando:
#   1.  quando forem executadas todas as instruções (pela ordem de 
#       introdução)
#   2.  quando uma dessas instruções termina explicítamente o script
#       (sys.exit())
#   (3. Quando ocorrer um erro fatal -> Exception)
#
# Nomes dos scripts de Python terminam sempre com extensão ".py"
#
# print =>  função (conjunto de instruções com nome) cujo nome é "print"
#           e que é responsável por enviar informação para a consola de
#           de texto (STANDARD OUTPUT). O "print" separa os argumentos 
#           com espaço.
#
# Todas as funções devem ser executadas da seguinte forma:
#
#       NOME_FUNCAO(ARG0, ARG1, ..., ARG_N)
#
# No nosso "print", temos apenas um argumento que é o texto "Olá, Mundo!"
# Ou seja, "Olá, Mundo" corresponde a ARG0.
# O número de argumentos que cada função aceita, depende da função
# em questão. Há funções que aceitam um número variável de argumentos 
# - caso do print -, outras aceitam apenas 1 argumentos, outras aceitam 2,
# outras 3, etc., e outras não aceitam nenhum.
#
# "Olá, Mundo!" =>  texto que nós queremos apresentar ao utilizador. 
#                   Em Python, utilizamos o tipo de dados "str" (string) 
#                   para representar texto. Ou seja, o print vai exibir
#                   a string "Olá, Mundo"
#
# tipo de dados =>  toda a informação (dados) processada pelo Python é 
#                   etiquetada com um tipo de dados, ie, com uma indicação
#                   respeitante à estrutura da própria informação
#
# string        =>  sequência de 0 ou mais caracteres. Representamos os 
#                   caracteres da string entre aspas (") ou plicas (').
#                   Em Python, este tipo de dados é identificado por str .

# plica         =>  apóstrofos em informatiquês

print("Olá, Mundo!")
