import math
from sympy.solvers import solve
from sympy import Symbol, solve, sympify

class Main():
    matriz = None
    matriz2 = None
    matriz3 = None

    def __init__(self, linhas):

        self.linhas_matriz = linhas
        self.elementos_matriz = self.linhas_matriz ** 2

        self.linhas_matriz2 = linhas
        self.elementos_matriz2 = self.linhas_matriz2 ** 2

        if Main.matriz is None:
            Main.matriz = [0] * self.elementos_matriz

        if Main.matriz2 is None:
            Main.matriz2 = [0] * self.elementos_matriz

        if Main.matriz3 is None:
            Main.matriz3 = [0] * self.elementos_matriz

#########################################################################################################################################

    def lista_matriz_preview(self): #print das posições da matriz 
        Main.matriz_preview = list(range(self.elementos_matriz))
        print("Essa é o tamanho de matriz que você escolheu: ")
        for linhas in range(self.linhas_matriz):
            linha_formatada = " | ".join([f"{str(Main.matriz_preview[(linhas * self.linhas_matriz) + i]).rjust(4)}" for i in range(self.linhas_matriz)])
            print(f"| {linha_formatada} |")

#########################################################################################################################################    

    def definir_valores_matriz(self, escolha): 
        if escolha == 0: #Função que você pode editar duas matrizes 
            matriz = 1
            print("Matriz 1")
            while matriz == 1:
                self.lista_matriz_preview()
                
                while True:
                    val = int(input("Digite o número da posição que você quer alterar:\n")) 
                    valor = int(input("Digite o valor que você quer atribuir a essa posição:\n")) 
                    try:
                        Main.matriz[val] = valor
                        break
                    except Exception as e:
                        print(f"Erro: {e}")
                
                for linhas in range(self.linhas_matriz):
                    linha_formatada = " | ".join([f"{str(Main.matriz[(linhas * self.linhas_matriz) + i]).rjust(4)}" for i in range(self.linhas_matriz)])
                    print(f"| {linha_formatada} |") 
                
                satisfeito = input("Você está satisfeito com a matriz 1? (Sim/Nao)\n")
                if satisfeito == "Sim":
                    matriz = 2
                elif satisfeito == "Nao":
                    print("Ok, vamos continuar alterando a matriz.")
                else:
                    print("Digite uma resposta válida")
                
                
                print("Matriz 2")
                while True:
                    self.lista_matriz_preview()
                    
                    val = int(input("Digite o número da posição que você quer alterar:\n"))
                    valor = int(input("Digite o valor que você quer atribuir a essa posição:\n"))
                    try:
                        Main.matriz2[val] = valor
                        break
                    except Exception as e:
                        print(f"Erro: {e}")
                    
                    for linhas in range(self.linhas_matriz):
                        linha_formatada = " | ".join([f"{str(Main.matriz2[(linhas * self.linhas_matriz2) + i]).rjust(4)}" for i in range(self.linhas_matriz2)])
                        print(f"| {linha_formatada} |")

                    satisfeito = input("Você está satisfeito com a matriz 1? (Sim/Nao)\n")
                    if satisfeito == "Sim":
                        break
                    elif satisfeito == "Nao":
                        print("Ok, vamos continuar alterando a matriz.")
                    else:
                        print("Digite uma resposta válida")
                        
            return Main.matriz, Main.matriz2

#########################################################################################################################################
        
        elif escolha == 1: #Função que você pode editar apenas uma matriz
            matriz = 1
            while matriz == 1:
                self.lista_matriz_preview()
                
                while True:
                    val = int(input("Digite o número da posição que você quer alterar:\n")) #posicao
                    valor = int(input("Digite o valor que você quer atribuir a essa posição:\n")) #valor
                    try:
                        Main.matriz[val] = valor
                        break
                    except Exception as e:
                        print(f"Erro: {e}")
                
                for linhas in range(self.linhas_matriz):
                    linha_formatada = " | ".join([f"{str(Main.matriz[(linhas * self.linhas_matriz) + i]).rjust(4)}" for i in range(self.linhas_matriz)])
                    print(f"| {linha_formatada} |") #representacao

                satisfeito = input("Você está satisfeito com a matriz 1? (Sim/Nao)\n")
                if satisfeito == "Sim":
                    break
                elif satisfeito == "Nao":
                    print("Ok, vamos continuar alterando a matriz.")
                else:
                    print("Digite uma resposta válida")
                    
            return Main.matriz
        
#########################################################################################################################################
        
        elif escolha == 2: #Função que você pode alterar uma matriz e a outra é uma identidade 
            print("Escolha 2")
            matriz = 1
            while matriz == 1:
                self.lista_matriz_preview()
                
                while True:
                    val = int(input("Digite o número da posição que você quer alterar:\n"))
                    valor = int(input("Digite o valor que você quer atribuir a essa posição:\n"))
                    try:
                        Main.matriz[val] = valor
                        break
                    except Exception as e:
                        print(f"Erro: {e}")
                
                for linhas in range(self.linhas_matriz):
                    linha_formatada = " | ".join([f"{str(Main.matriz[(linhas * self.linhas_matriz) + i]).rjust(4)}" for i in range(self.linhas_matriz)])
                    print(f"| {linha_formatada} |")

                satisfeito = input("Você está satisfeito com a matriz 1? (Sim/Nao)\n")
                if satisfeito == "Sim":
                    break
                elif satisfeito == "Nao":
                    print("Ok, vamos continuar alterando a matriz.")
                else:
                    print("Digite uma resposta válida")
            
            for i in range(0, len(Main.matriz), self.linhas_matriz+1):
                Main.matriz2[i] = "x"
                
            return Main.matriz, Main.matriz2 
        
#########################################################################################################################################

class Operacoes(Main):
    def __init__(self, linhas):
        super().__init__(linhas)
        
    def soma_matriz(self):
        for i in range(len(Main.matriz)):
            Main.matriz3[i] = Main.matriz[i] + Main.matriz2[i]
        return Main.matriz3     
        
    def subtr_matriz(self):
        for i in range(len(Main.matriz)):
            Main.matriz3[i] = Main.matriz[i] - Main.matriz2[i]
        return Main.matriz3
            
    def subtr_matriz_str(self):
        for i in range(len(Main.matriz)):
            Main.matriz3[i] = f"({Main.matriz[i]} - {Main.matriz2[i]})"
        return Main.matriz3
        
    def expansao_matriz(self):  
        matriz_expandida = []
        
        for i in range(self.linhas_matriz):
            inicio_linha = i * self.linhas_matriz
            linha_original = Main.matriz[inicio_linha:inicio_linha + self.linhas_matriz]
            matriz_expandida.extend(linha_original)
            
            matriz_expandida.append(linha_original[0])
            matriz_expandida.append(linha_original[1])
        
        return matriz_expandida
    
    #########################################################################################################################################
    
    def determinante_matriz(self):
        lista_operadora = []
        matriz_expandida = self.expansao_matriz()
        linhas = self.linhas_matriz
        
        produtos1 = []
        produtos2 = []
        
        for a in range(self.linhas_matriz-1): 
            lista_operadora_sub = []
            
            for b in range(linhas): 
                val = (b*((linhas*2)-(linhas-3))) + a
                lista_operadora_sub.append(val)
                
            lista_operadora.append(lista_operadora_sub)
        
        try:
            for op in lista_operadora:
                op = [matriz_expandida[prod] for prod in op]
                produto = math.prod(op)
                produtos1.append(produto)
            
        except Exception as E:
            print(f"Erro {E}")
            
        soma1 = sum(produtos1) 
        
        lista_operadora.clear() 
                
        for a in range(self.linhas_matriz-1): 
            lista_operadora_sub = []
            
            for b in range(linhas): 
                val = (b * (linhas + 1)) + (a+(linhas-1))
                lista_operadora_sub.append(val) 
                
            lista_operadora.append(lista_operadora_sub)
        
        try:
            for op in lista_operadora:
                op = [matriz_expandida[prod] for prod in op]
                produto = math.prod(op)
                produtos2.append(produto)
            
        except Exception as E:
            print(f"Erro {E}")
            
        soma2 = sum(produtos2) 
        
        determinante = soma1 - soma2
            
        return determinante
    
#########################################################################################################################################
    def expansao_matriz_str(self):
        matriz = self.subtr_matriz_str()
        matriz_expandida = []
        
        for i in range(self.linhas_matriz):
            inicio_linha = i * self.linhas_matriz
            linha_original = matriz[inicio_linha:inicio_linha + self.linhas_matriz] #pega os valores da matriz3
            matriz_expandida.extend(linha_original)
            
            matriz_expandida.append(linha_original[0])
            matriz_expandida.append(linha_original[1])

        return matriz_expandida                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          

#########################################################################################################################################        
    def determinante_matriz_str(self):
        lista_operadora = []
        matriz_expandida_str = self.expansao_matriz_str()
        linhas = self.linhas_matriz
        
        equacao1 = ""
        equacao2 = ""
        
        for a in range(self.linhas_matriz-1): 
            lista_operadora_sub = []
            for b in range(linhas): 
                val = (b*((linhas*2)-(linhas-3))) + a
                lista_operadora_sub.append(val)
                
            lista_operadora.append(lista_operadora_sub)
        
        try: 
            for op in lista_operadora:
                termos = [f"{matriz_expandida_str[prod]}" for prod in op]
                produto_str = "*".join(termos)
                equacao1 += f"({produto_str}) + "
            
        except Exception as E:
            print(f"Erro {E}")

        equacao1 = equacao1.rstrip(" + ")
        
        lista_operadora.clear() 
                
        for a in range(self.linhas_matriz-1): 
            lista_operadora_sub = []
            
            for b in range(linhas):
                val = (b * (linhas + 1)) + (a+(linhas-1))
                lista_operadora_sub.append(val)
                
            lista_operadora.append(lista_operadora_sub)

        try: 
            for op in lista_operadora:
                termos = [f"{matriz_expandida_str[prod]}" for prod in op]
                produto_str = "*".join(termos)
                equacao2 += f"({produto_str}) + "
        
        except Exception as E:
            print(f"Erro {E}")
        
        equacao2 = equacao2.rstrip(" + ")
        
        equacao_final = f"({equacao1}) - ({equacao2})"
        
        return equacao_final
        
#########################################################################################################################################
    def autovalor_matriz(self):
        equacao = self.determinante_matriz_str()
        x = Symbol("x")
        try:
            eq = sympify(equacao)
            
            sol = solve(eq, x)
        
        except Exception as E:
            return print(f"Erro {E}")
        
        print("Os autovalores da matriz escolhida são:")
        for i in sol:
            print(f"x = {i}")
        return sol

#########################################################################################################################################
    def autovetor_matriz(self):
        # Obter os autovalores
        valores_x = self.autovalor_matriz()
        matriz = Main.matriz  #Matriz principal
        n = self.linhas_matriz  #Quantidade de linhas
        autovetores = {}

        for autovalor in valores_x:
            try:
                matriz_lambda = [
                    [
                        matriz[i * n + j] - (autovalor if i == j else 0)
                        for j in range(n)
                    ]
                    for i in range(n)
                ]

                # Resolver o sistema
                vetor_solucao = [0] * n  
                linha_pivo = 0  

                for coluna in range(n):
                    # Encontrar a linha de pivô
                    for linha in range(linha_pivo, n):
                        if matriz_lambda[linha][coluna] != 0:
                            # Trocar a linha atual com a linha de pivô
                            matriz_lambda[linha], matriz_lambda[linha_pivo] = (
                                matriz_lambda[linha_pivo],
                                matriz_lambda[linha],
                            )
                            break

                    # Escalonamento
                    for linha in range(linha_pivo + 1, n):
                        if matriz_lambda[linha][coluna] != 0:
                            fator = matriz_lambda[linha][coluna] / matriz_lambda[linha_pivo][coluna]
                            for k in range(n):
                                matriz_lambda[linha][k] -= fator * matriz_lambda[linha_pivo][k]

                    linha_pivo += 1

                # Determinar o autovetor a partir do sistema escalonado
                vetor_solucao = [0] * n
                for i in range(n - 1, -1, -1):
                    soma = sum(matriz_lambda[i][j] * vetor_solucao[j] for j in range(i + 1, n))
                    if matriz_lambda[i][i] != 0:
                        vetor_solucao[i] = -soma / matriz_lambda[i][i]
                    else:
                        vetor_solucao[i] = 1  

                # Normalizar o vetor solução
                autovetores[autovalor] = [round(v, 3) for v in vetor_solucao]

            except Exception as e:
                print(f"Erro ao calcular autovetor para λ={autovalor}: {e}")
                
        print("\nResultado - Autovalores e Autovetores:") #Representação visual do resultado
        for autovalor, autovetor in autovetores.items():
            vetor_formatado = " | ".join([f"{v:.3f}" for v in autovetor])
            print(f"x = {autovalor} -> [ {vetor_formatado} ]")

        return autovetores
        
class Resultado(Operacoes):
    def __init__(self, linhas):
        super().__init__(linhas)
    
    def print_matriz(self):
        for linhas in range(self.linhas_matriz):
            linha_formatada = " | ".join([f"{str(Main.matriz3[(linhas * self.linhas_matriz) + i]).rjust(4)}" for i in range(self.linhas_matriz)])
            print(f"| {linha_formatada} |")
