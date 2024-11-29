import math

class Main():
    
    matriz = None
    matriz2 = None
    matriz3 = None
    
    def __init__(self, linhas, linhas1):
        self.linhas_matriz = linhas
        self.elementos_matriz = self.linhas_matriz ** 2
        
        self.linhas_matriz2 = linhas1
        self.elementos_matriz2 = self.linhas_matriz2 ** 2
        
        if Main.matriz is None:
            Main.matriz = [0] * self.elementos_matriz
            
        if Main.matriz2 is None:
            Main.matriz2 = [0] * self.elementos_matriz
            
        if Main.matriz3 is None:
            Main.matriz3 = [0] * self.elementos_matriz
            
        print(self.linhas_matriz, "linhas")

    
    def lista_matriz_preview(self):
        Main.matriz_preview = list(range(self.elementos_matriz))
        print("Essa é o tamanho de matriz que você escolheu: ")
        for linhas in range(self.linhas_matriz):
            linha_formatada = " | ".join([f"{str(Main.matriz_preview[(linhas * self.linhas_matriz) + i]).rjust(4)}" for i in range(self.linhas_matriz)])
            print(f"| {linha_formatada} |")
    
    
    def definir_valores_matriz(self): 
        print("Matriz 1")
        matriz = 1
        while matriz == 1:
            self.lista_matriz_preview()
            while True:
                val = int(input("Digite o número da posição que você quer alterar:\n")) #posicao
                valor = int(input("Digite o valor que você quer atribuir a essa posição:\n")) #valor
                try:
                    Main.matriz[val] = valor
                    break
                except Exception:
                    print("Digite um valor ou posição válida")
            
            for linhas in range(self.linhas_matriz):
                linha_formatada = " | ".join([f"{str(Main.matriz[(linhas * self.linhas_matriz) + i]).rjust(4)}" for i in range(self.linhas_matriz)])
                print(f"| {linha_formatada} |") #representacao

            satisfeito = input("Você está satisfeito com a matriz 1? (Sim/Nao)\n")
            if satisfeito == "Sim":
                matriz = 2
            elif satisfeito == "Nao":
                print("Ok, vamos continuar alterando a matriz.")
            else:
                print("Digite uma resposta válida")
    
        if matriz == 2: #alterando a matriz 2
            print("Matriz 2")
            while True:
                self.lista_matriz_preview()
                val = int(input("Digite o número da posição que você quer alterar:\n"))
                valor = int(input("Digite o valor que você quer atribuir a essa posição:\n"))
                try:
                    Main.matriz2[val] = valor
                    break
                except Exception:
                    print("Digite um valor ou posição válida")
                
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
        
        else:
            print("Escolha uma opção válida.")
        
        print(Main.matriz, Main.matriz2, "matrizes") #retorna as matrizes 
    
class Operacoes(Main):
    def __init__(self, linhas, linhas1):
        super().__init__(linhas, linhas1)
        
        
    def soma_matriz(self):
        for i in range(len(Main.matriz)): #index na lista ,  
            Main.matriz3[i] = Main.matriz[i] + Main.matriz2[i] #soma cada index      
        
    def subtr_matriz(self):
        for i in range(len(Main.matriz)):
            Main.matriz3[i] = Main.matriz[i] - Main.matriz2[i]
            
    def identidade_matriz(self):
        for i in range(0, len(Main.matriz), self.linhas_matriz+1):
            Main.matriz2[i] = 1

    def expansao_matriz(self):
        matriz_expandida = []
        #expandindo a matriz
        for i in range(self.linhas_matriz):
            inicio_linha = i * self.linhas_matriz
            linha_original = Main.matriz[inicio_linha:inicio_linha + self.linhas_matriz]
            matriz_expandida.extend(linha_original)
            
            # Adiciona as duas primeiras colunas da linha original ao final
            matriz_expandida.append(linha_original[0])  # Primeira coluna
            matriz_expandida.append(linha_original[1])  # Segunda coluna
        print("Matriz Original:", Main.matriz)
        print("Matriz Expandida:", matriz_expandida)
        print("Tamanho da Matriz Expandida:", len(matriz_expandida))
        return matriz_expandida
    
    def determinante_matriz(self):
        lista_operadora = []
        matriz_expandida = self.expansao_matriz()
        linhas = self.linhas_matriz
        produtos1 = []
        produtos2 = []
        
        for a in range(self.linhas_matriz-1): #numero de produtos a serem somados ex: 4 (diagonais = 3)
            lista_operadora_sub = []
            for b in range(linhas): #numeros no produto ex: 4
                val = (b*((linhas*2)-(linhas-3))) + a
                lista_operadora_sub.append(val)
            lista_operadora.append(lista_operadora_sub)
        
        print(lista_operadora)
        try:
            for op in lista_operadora:
                op = [matriz_expandida[prod] for prod in op]
                print(op)
                produto = math.prod(op)
                produtos1.append(produto)
            
        except Exception as E:
            print(f"Erro {E}")
        print(produtos1)
        soma1 = sum(produtos1) #primeira soma
        
        lista_operadora.clear() #limpa a lista para receber mais produtos
                
        for a in range(self.linhas_matriz-1): #numero de produtos a serem somados ex: 3
            lista_operadora_sub = []
            for b in range(linhas): #numeros no produto ex: 3
                val = (b * (linhas + 1)) + (a+(linhas-1))
                lista_operadora_sub.append(val)
            lista_operadora.append(lista_operadora_sub)
        
        print(lista_operadora)
        try:
            for op in lista_operadora:
                op = [matriz_expandida[prod] for prod in op]
                print(op)
                produto = math.prod(op)
                print(produto)
                produtos2.append(produto)
            
        except Exception as E:
            print(f"Erro {E}")
        print(produtos2)
        soma2 = sum(produtos2) #primeira soma
        
        print(soma1, soma2, "soma1 e soma2")
        
        determinante = soma1 - soma2
        
        print(determinante)
        #Formula determinante = soma1 - soma2                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               
                
        
class Resultado(Operacoes):
    def __init__(self, linhas, linhas1):
        super().__init__(linhas, linhas1)
    
    def print_matriz(self):
        for linhas in range(self.linhas_matriz):
            linha_formatada = " | ".join([f"{str(Main.matriz3[(linhas * self.linhas_matriz) + i]).rjust(4)}" for i in range(self.linhas_matriz)])
            print(f"| {linha_formatada} |")

# 0 1 2 3 
# 4 5 6 7
# 8 9 10 11
# 12 13 14 15