from Funcoes import *


linhas = int(input("Digite o tamanho da sua primeira matriz. Ex:. 4 -> 4x4\n"))

linhas1 = int(input("Digite o tamanho da sua segunda matriz. Ex:. 4 -> 4x4\n"))

calculadora = Main(linhas, linhas1)

resultado = Resultado(linhas, linhas1)

operacao = Operacoes(linhas, linhas1)

calculadora.definir_valores_matriz() #iniciar a calculadora

operacao.determinante_matriz()

resultado.print_matriz()

