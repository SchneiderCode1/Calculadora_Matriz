from Funcoes import *



print("Calculadora de Matrizes\nLimitações:\nA calculadora só é capaz de realizar suas operações padrão em matrizes quadradas de tamanho mínimo 3x3.\n")

linhas = int(input("Digite o tamanho da(s) matriz(es). Ex:. 4 -> 4x4\n"))

calculadora = Main(linhas)
resultado = Resultado(linhas)
operacao = Operacoes(linhas)


while True:
    try:
        escolha =  int(input("Selecione o número da operação a ser realizada: Soma (1), Subtração (2), Determinante (3), Autovalor e Autovetor (4).\n" ))
        if escolha == 1: #Soma
            escolha = 0
            calculadora.definir_valores_matriz(escolha) 
            resultado.soma_matriz()
            break

        elif escolha == 2: #Subtração
            escolha = 0
            calculadora.definir_valores_matriz(escolha) 
            resultado.subtr_matriz()
            break

        elif escolha == 3: #Determinante 
            escolha = 1
            calculadora.definir_valores_matriz(escolha) 
            resultado.determinante_matriz()
            break

        elif escolha == 4: #Autovetor
            escolha = 2
            calculadora.definir_valores_matriz(escolha) 
            operacao.autovetor_matriz()
            break

    except ValueError:
        print("Escolha umas das opções disponíveis.")