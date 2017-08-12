from numpy import matrix
from numpy import linalg
import math

class Matriz: ## Define o que e uma matriz
    def __init__(self, matriz): ## Roda ao criar a matriz
        self.matriz = matriz ## Matriz
        self.check() ## Verifica se a matriz esta correta
        
    def check(self): ## Funcao que verifica se a matriz esta correta
        for line in self.matriz: # Para cada linha da matriz
            if len(line) == len(self.matriz[0]): ## Verifica se a linha tem o mesmo numero de elementos que a primeira linha
                return True
            else:
                print('erro') #####################################
                return ## Deve retornar um erro

    def print(self): ## Funcao para printar matriz
        for line in self.matriz: ## Printa linha por linha
            print(line)

    def trans(self): ## Funcao que retorna matriz transposta
        trans = [] ## Cria uma lista que posteriormente sera transformada na matriz
        for column in range(0,len(self.matriz[0])): ## Para cada coluna c na matriz original
            trans.append([]) ## Adiciona uma linha a lista 'trans'
            for line in range(0,len(self.matriz)): ## Para cada linha l na matriz original
                trans[column].append(self.matriz[line][column]) ## Transforma essa linha l da matriz original na coluna c da matriz transposta
        return Matriz(trans) ## Retorna matriz transposta

    def inv(self,method='np'): ## Inverte a matriz pelo metodo selecionado
        if method.lower() == 'np':
            return self.inv_np()
        elif method.upper() == 'GJ':
            return self.inv_GJ()
        else:
            pass
        
    def inv_np(self): ## Inverte a matriz usando numpy
        np_mat = matrix(self.matriz) ## Copia a matriz a ser invertida para o numpy
        inv_np = np_mat.I ## Inverte a matriz pelo numpy
        inv = [] ## Cria uma lista vazia que se tornará a matriz inversa no programa
        for line in range(0,len(inv_np)): ## Para cada linha
            inv.append([]) ## Adiciona uma linha a matriz
            split_line = str(inv_np[line][0]).replace('[','').replace(']','').split(' ') ## Separa as entradas da linha da matriz
            for element in split_line: ## Para cada elemento na linha
                try:
                    float(element) ## Verifica se o elemento e um numero
                    inv[line].append(float(element)) ## Adiciona o elemento a matriz
                except:
                    pass
        return Matriz(inv) ## Tranforma a lista em matriz e retorna a matriz
        
    def inv_GJ(self): ## Inverte a matriz pelo metodo Gauss-Jordan -- Nao funcionando
        ident = [] ## Esta lista se tornara a matriz identidade
        copy = [] ## Essa matriz ira copiar a matriz que sera invertida
        for i in range(0,len(self.matriz)): ## Vamos contruir as matrizes copy e ident
            ident.append([]) ## Adiciona uma linha a matriz
            copy.append([]) ## Adiciona uma linha a matriz
            for j in range(0,len(self.matriz[0])):
                copy[i].append(self.matriz[i][j]) ## Copia o termo ij da matriz que sera invertida para a copia
                if i == j: ## Se i = j
                    ident[i].append(1) ## Adiciona o termo 1 ao espaço ij da matriz
                else: ## Se i =! j
                    ident[i].append(0) ## Adiciona o termo 0 ao espaço ij da matriz
        ident = Matriz(ident) ## Transforma as listas em matrizes
        copy = Matriz(copy) ## Vamos agora aplicar o metodo Gauss-Jordan
        ## O primeiro passo e fazer com que todos os elementos da matriz fora da diagonal principal se tornem zeros
        lines_to_iterate = []
        for n in range(0,len(copy.matriz)):
            lines_to_iterate.append(n)
        while len(lines_to_iterate) > 0:
            for line in lines_to_iterate: ## Cada linha rodara a iteracao uma vez
                if copy.matriz[line][line] != 0:
                    for i in range(0,len(copy.matriz)): ## Em todas as outras linhas
                        if copy.matriz[i] != copy.matriz[line]: ## Somente as OUTRAS linhas (nao ela mesma)
                            f = copy.matriz[i][line]/copy.matriz[line][line]## Obtem o fator de multiplicacao entre a linha principal e a linha 'alvo'
                            for j in range(0,len(copy.matriz[0])):
                                copy.matriz[i][j] = copy.matriz[i][j] - f*copy.matriz[line][j] ## Li = Li - f*Lline
                                ident.matriz[i][j] = ident.matriz[i][j] - f*ident.matriz[line][j]                                
                lines_to_iterate.remove(line)
                

        
        for i in range(0,len(copy.matriz)):
            f = 1/copy.matriz[i][i]
            for j in range(0,len(copy.matriz[0])):
                copy.matriz[i][j] = f*copy.matriz[i][j]
                ident.matriz[i][j] = round(f*ident.matriz[i][j],5)
        return ident
            

def msum(l):
    try:
        for matriz in l: ## Para cada matriz na lista
            if len(matriz.matriz) == len(l[0].matriz) and len(matriz.matriz[0]) == len(l[0].matriz[0]): ## Verifica se as matrizes sao do mesmo tamanho da primeira matriz
                pass
            else:
                raise NameError ## Caso contrario a funcao para
        ## Agora comecamos a soma das matrizes
        msum = [] ## Cria uma lista vazia que ira armazenar a soma, que posteriormente sera transformado na matriz resultante
        for line in range(0,len(l[0].matriz)): ## Para cada linha
            msum.append([]) ## Adiciona uma linha a matriz da soma
            for column in range(0,len(l[0].matriz[0])): ## Para cada linha
                s = 0 ## Zera o valor de s (que corresponde a soma dos termos ij das matrizes
                for i in l: ## Para cada matriz que esta sendo somada
                    s = s + i.matriz[line][column] ## Adiciona-se a s o termo ij de cada matriz
                msum[line].append(s) ## Adiciona-se a soma dos termos de indice ij ao espaço ij da matriz resultante
        return Matriz(msum)  ## Retorna a matriz da soma
    except:
        pass
            
def mult(A, B): ## Produto matriz x matriz, matriz x escalar e escalar x matriz
    try:
        if A.check() == True and B.check() == True: ## Produto matriz x matriz
            if len(A.matriz[0]) == len(B.matriz): ## Verifica se o numero de linhas de colunas de A e igual ao numero de linhas de B
                prod = [] ## Cria uma lista vazia que ira armazenar o produto, que posteriormente sera transformado na matriz resultante
                for i in range(0,len(A.matriz)): ## Para cada linha i na matriz A
                    prod.append([]) ## Cria-se uma linha na matriz produto
                    for j in range(0,len(B.matriz[0])): ## Para cada coluna na matriz B
                        n = 0 ## Começa a calcular o valor do elemento ij da matriz produto
                        for c in range(0,len(A.matriz[0])): ## Cria-se a variavel c, que corre da primeira a ultima linha em A/coluna em B
                            n = n + A.matriz[i][c]*B.matriz[c][j] ## Soma-se a n o produto entre o elemento de A com indice ic e o elemento de B com indice cj
                        prod[i].append(n) ## Adiciona o elemento de indice ij a matriz do produto
            return Matriz(prod) ## Retorna a matriz do produto
    except:
        pass

    try:
        if A.check() == True and type(B) == type(int(1)) or A.check() == True and type(B) == type(float(1)): ## Produto matriz x escalar
            prod = [] ## Cria uma lista vazia que ira armazenar o produto, que posteriormente sera transformado na matriz resultante
            for line in range(0,len(A.matriz)): ## Para cada linha na matriz A
                prod.append([]) ## Adiciona uma linha a matriz do produto
                for column in range(0,len(A.matriz[0])): ## Para cada coluna da matriz A
                    prod[line].append(B*A.matriz[line][column]) ## Multiplica-se o elemento da linha/coluna de A pelo escalar B
            return Matriz(prod) ## Retorna a matriz do produto
    except:
        pass

    try:
        if B.check() == True and type(A) == type(int(1)) or B.check() == True and type(A) == type(float(1)): ## Produto escalar x matriz
            prod = [] ## Cria uma lista vazia que ira armazenar o produto, que posteriormente sera transformado na matriz resultante
            for line in range(0,len(B.matriz)): ## Para cada linha na matriz B
                prod.append([]) ## Adiciona uma linha a matriz do produto
                for column in range(0,len(B.matriz[0])): ## Para cada coluna da matriz B
                    prod[line].append(A*B.matriz[line][column]) ## Multiplica-se o elemento da linha/coluna de B pelo escalar A
            return Matriz(prod) ## Retorna a matriz do produto
    except:
        pass
    



    
#A = Matriz([[1, 1, 1],
            #[2, 4, 6],
            #[2, 2, 2]])
#B = float(1)

#B = Matriz([[1, 1, 1],
            #[0, 0, 0],
            #[0, 2, 3]])

#B = Matriz([[2, -1, 1],
            #[-1, 2, -1],
            #[0, -1, 2]])

#B.inv()
