## Carregar modulos de outros arquivos
import math ## Modulo com funcoes matematicas
import loadParameters as loadp ## Modulo que carrega os parametros do problema
import fiberLoad as loadf ## Modulo que carrega os parametros da fibra
import Matriz as m ## Modulo que define matrizes
import unitConverter as c ## Conversor de unidade


## Comeca a carregar os parametros do problema
parameters = loadp.parametersLoad('Trabalho_semicontinuo')
d_unit = parameters[0]
d = c.convert(d_unit, 'mm', float(parameters[1])) ## Converte da unidade do arquivo para unidade conveniente
matriz = parameters[2]
fiber_name = parameters[3]
layers = int(parameters[4])
layers_thickness_unit = parameters[5]
layers_thickness = c.convert(layers_thickness_unit, 'mm', float(parameters[6]))
teta_unit = parameters[7]
teta_interval = parameters[8]
## Iteracao para obter os angulos teta
l = parameters[9].split(',')
teta = []
if teta_interval.lower() == 'discreto':
    for i in l:
        teta.append(c.convert(teta_unit, 'rad', float(i)))
elif teta_interval.lower() == 'continuo' and len(l) == 2:
    for i in range(int(l[0]), int(l[1])+1, 1):
        teta.append(c.convert(teta_unit, 'rad', float(i)))
## Angulos teta obtidos
## Iteracao para obter o modo de organizacao dos angulos
l = parameters[10].split(',')
angles = []
for i in l:
    angles.append(float(i))
## Organizacao dos angulos obtida
Pmax = {} ## Dicionario que registrara a pressao maxima correspondente a cada angulo, sera usado no final do programa
## Terminou de carregar os parametros do problema

## Comeca a carregar os parametros da fibra
fiber = loadf.fiberLoad(fiber_name)
E1 = fiber[0]
E2 = fiber[1]
G12 = fiber[2]
v12 = fiber[3]
Xt = fiber[4]
Xc = fiber[5]
Yt = fiber[6]
Yc = fiber[7]
S12 =  fiber[8]
## Terminou de carregar os parametros da fibra

## Obter coordenadas z das camadas
z = [] ## Cria lista vazia com alturas
height = 0 ## Altura total
for layer in range(0,layers): ## Para cada camada
    z.append(height) ## Anota o valor da altura da camada
    height = height+layers_thickness ## Passa para a altura da proxima camada
z.append(height) ## Anota o valor da altura mais alta (a ultima, pois tem-se uma altura a mais que o numero de camadas)
for i in range(0,len(z)): ## Agora vamos centralizar a coordenada da altura
    z[i] = z[i]-height/2 ## Desloca cada coordenada z a uma distancia igual a altura total/2, de modo que agora o intervalo de z vai de -h/2 a h/2 ao inves de 0 a h
## Coordendas z das camadas obtidas

## Cria a matriz Q da fibra
Q11 = E1/(1-(v12**2)*E2/E1)  ## Calcula Q11
Q12 = v12*E2/(1-(v12**2)*E2/E1) ## Calcula Q12
Q21 = Q12 ## Calcula Q21, que e igual a Q12
Q22 = E2/(1-(v12**2)*E2/E1) ## Calcula Q22
Q33 = G12 ## Calcula Q33
Q = m.Matriz([[Q11,Q12,0],
              [Q21,Q22,0],
              [0,0,Q33]])
## Matriz Q criada
Ql_all = {}
## Criar matrizes de rotacao T
Tlist = {} ## Cria um dicionario que terá o T de cada angulo que podera ser usado
for t in teta: ## A partir de agora, o problema e resolvido para cada teta
    for ang in angles: ## A iteracao a seguir calcula todos os angulos que serao usados na resolucao do problema
        if t*ang in Tlist:
            pass
        else:
            T11 = round((math.cos(t*ang))**2,5); T12 = round((math.sin(t*ang))**2,5); T13 = round(2*math.sin(t*ang)*math.cos(t*ang),5)
            T21 = round((math.sin(t*ang))**2,5); T22 = round((math.cos(t*ang))**2,5); T23 = round(-2*math.sin(t*ang)*math.cos(t*ang),5)
            T31 = round(-math.sin(t*ang)*math.cos(t*ang),5); T32 = round(math.sin(t*ang)*math.cos(t*ang),5); T33 = round((math.cos(t*ang))**2 - (math.sin(t*ang))**2,5)
            Tlist[t*ang] = m.Matriz([[T11, T12, T13],
                                     [T21, T22, T23],
                                     [T31, T32, T33]])
## Matrizes de rotacao T criadas

## Obter matrizes Q'
    Ql_list = []
    for layer in range(0,layers):
        Ql_list.append(m.mult(m.mult(Tlist[t*angles[layer]].inv(),Q),Tlist[t*angles[layer]].inv().trans()))
        if t*angles[layer] not in Ql_all:
            Ql_all[t*angles[layer]] = m.mult(m.mult(Tlist[t*angles[layer]].inv(),Q),Tlist[t*angles[layer]].inv().trans())
## Matrizes Q' obtidas

## Obter matrizes ABD
    ## Obtendo matriz A
    A = m.Matriz([[0, 0, 0], ## Cria uma matriz de zeros chamada A
                  [0, 0, 0],
                  [0, 0, 0]])
    for layer in range(0,layers): ## Para cada camada
        A = m.msum([A,m.mult(Ql_list[layer],(z[layer+1]-z[layer]))]) ## Adiciona a A o produto entre Ql e (Zn+1 - Zn)
    ## Matriz A calculada
    ## Obtendo matriz B
    B = m.Matriz([[0, 0, 0], ## Cria uma matriz de zeros chamada B
                  [0, 0, 0],
                  [0, 0, 0]])
    for layer in range(0,layers): ## Para cada camada
        B = m.msum([B,m.mult(Ql_list[layer],(z[layer+1]**2-z[layer]**2)/2)]) ## Adiciona a B o produto entre Ql e (Zn+1^2 - Zn^2)
    ## Matriz B calculada
    ## Obtendo matriz D
    D = m.Matriz([[0, 0, 0], ## Cria uma matriz de zeros chamada D
                  [0, 0, 0],
                  [0, 0, 0]])
    for layer in range(0,layers): ## Para cada camada
        D = m.msum([D,m.mult(Ql_list[layer],(z[layer+1]**3-z[layer]**3)/3)]) ## Adiciona a D o produto entre Ql e (Zn+1^2 - Zn^2)
    ## Matriz D calculada
## Construindo matriz ABD
    ABD = [] ## Cria uma lista que ira se tornar a matriz ABD
    for linha in range(0,3): ## Nas tres primeiras linhas
        ABD.append([]) ## A cada linha da iteracao cria-se uma linha
        for coluna in range(0,3): ## Nas primeiras tres colunas das tres primeiras linhas (espaço 3x3 no segundo quadrante)
            ABD[linha].append(A.matriz[linha][coluna]) ## Adiciona a entrada correspondente de A
        for coluna in range(0,3): ## Nas ultimas tres colunas das tres primeiras linhas (espaço 3x3 no primeiro quadrante)
            ABD[linha].append(B.matriz[linha][coluna]) ## Adiciona a entrada correspondente de B
    for linha in range(0,3): ## Nas tres ultimas linhas
        ABD.append([])
        for coluna in range(0,3): ## Nas primeiras tres colunas das tres ultimas linhas (espaço 3x3 no terceiro quadrante)
            ABD[linha+3].append(B.matriz[linha][coluna]) ## Adiciona a entrada correspondente de B
        for coluna in range(0,3): ## Nas ultimas tres colunas das tres ultimas linhas (espaço 3x3 no quarto quadrante)
            ABD[linha+3].append(D.matriz[linha][coluna]) ## Adiciona a entrada correspondente de D
    ABD = m.Matriz(ABD)
    ## Obtendo então a matriz
    ##  [A, A, A, B, B, B]
    ##  [A, A, A, B, B, B]
    ##  [A, A, A, B, B, B]
    ##  [B, B, B, D, D, D]
    ##  [B, B, B, D, D, D]
    ##  [B, B, B, D, D, D]
## Matrizes ABD obtidas

## Inverter ABD
    ABD_inv = ABD.inv()
## ABD invertida

## Obter carregamentos e deformacoes para maxima pressao
    P = 0
    step = 1/40
    while True:
        max_tension = [0, 0, 0]
        carregamento = m.Matriz([[P*d/4],
                                 [P*d/2],
                                 [0],
                                 [0],
                                 [0],
                                 [0]])

        def_cur = m.mult(ABD_inv, carregamento)
        layers_ten_def = [] ## Aqui serao guardados as tensoes e deformacoes de cada camada nas superficies superior e inferior
        for layer in range(0,layers):  ## Para cada camada
            layers_ten_def.append([]); layers_ten_def.append([]) ## Adiciona-se duas listas, uma para a superficie inferior[0] e uma para a superficie superior[1]
            layers_ten_def[-2].append(z[layer])   ## Cada superficie tem a sua altura em z
            layers_ten_def[-1].append(z[layer+1]) ## ...
            for line in [layers_ten_def[-2], layers_ten_def[-1]]: ## Em cada superficie obteremos uma linha de informacao
                ex = def_cur.matriz[0][0] + line[0]*def_cur.matriz[3][0]; line.append(ex) ## Obtem-se ex
                ey = def_cur.matriz[1][0] + line[0]*def_cur.matriz[4][0]; line.append(ey) ## Obtem-se ey
                Yxy = def_cur.matriz[2][0] + line[0]*def_cur.matriz[5][0]; line.append(Yxy) ## Obtem-se Yxy
                e_rot = m.mult(Tlist[t*angles[layer]].trans().inv(),m.Matriz([[ex],[ey],[Yxy]])) ## Obtem-se o e rotacionado
                line.append(e_rot.matriz[0][0]); line.append(e_rot.matriz[1][0]); line.append(e_rot.matriz[2][0]) ## Adiciona e_rot a linha de informacao
                tensoes = m.mult(Ql_list[layer],m.Matriz([[ex],[ey],[Yxy]])) ## Obtem as tensoes
                line.append(tensoes.matriz[0][0]); line.append(tensoes.matriz[1][0]); line.append(tensoes.matriz[2][0]) ## Adiciona as tensoes a linha de informacao
                tensoes_rot = m.mult(Tlist[t*angles[layer]],tensoes) ## Rotaciona as tensoes
                line.append(tensoes_rot.matriz[0][0]); line.append(tensoes_rot.matriz[1][0]); line.append(tensoes_rot.matriz[2][0]) ## Adiciona as tensoes rotacionadas a linha de informacoes
                
        for line in layers_ten_def: ## Agora vamos verificar quais são as tensoes maximas aplicadas nas camadas do composito
            if line[10] > max_tension[0]: ## Verifica tensao maxima em x
                max_tension[0] = max_tension[0] - max_tension[0] + line[10]
            if line[11] > max_tension[1]: ## Verifica tensao maxima em y
                max_tension[1] = max_tension[1] - max_tension[1] + line[11]
            if line[12] > max_tension[2]: ## Verifica tensao maxima em xy
                max_tension[2] = max_tension[2] - max_tension[2] + line[12]
        error_Nx = Xt - max_tension[0]; error_Ny = Yt - max_tension[1]
        if abs(error_Nx) < 0.1 or abs(error_Ny) < 0.1: ## Se a tensao resultante for aproximadamente igual a tensao maxima suportada pelo corpo
            Pmax[P] = round(c.convert('rad', 'graus', t),5) ## Adiciona a entrada correspondente ao angulo teta e pressao P
            break                                           ## E finaliza o loop para esse angulo
        else:                                          ## Se a tensao resultante nao e igual a tensao maxima suportada
            P = P + step*min(error_Nx, error_Ny)       ## A pressao da um passo na direcao necessaria
## Carregamentos e deformacoes obtidos

        
