## Exemplo 1
resultados_arquivo = open('Resultados.txt', 'r')
resultados = resultados_arquivo.readlines()
resultados_arquivo.close()

dezenas = {}
for dezena in range(1,61):
    dezenas[dezena] = 0

for resultado in resultados:
    resultado = resultado.replace('\n', '')
    resultado = resultado.split('\t')
    if '' not in resultado:
        for i in range(1,len(resultado)):
            dezena = int(resultado[i])
            dezenas[dezena] += 1

print '%7s %21s' % ('Dezenas', 'Ocorrencias')
for i in dezenas:
    print '  %02d %23d' % (i, dezenas[i])





## Exemplo 2
## Carregar resultados
resultados_arquivo = open('Resultados.txt', 'r')
resultados = resultados_arquivo.readlines()
resultados_arquivo.close()


## Escolher dezenas
dezenas_escolhidas = []
while len(dezenas_escolhidas) < 6:    
    escolha = raw_input('Escolha sua %da dezena: ' % (len(dezenas_escolhidas) + 1))
    if escolha.isdigit() and int(escolha) not in dezenas_escolhidas and int(escolha) in range(1,61):
        dezenas_escolhidas.append(int(escolha))
        
    elif escolha.isdigit() and int(escolha) in dezenas_escolhidas:
        print 'Essa dezena ja foi escolhida'
        
    elif escolha.isdigit() and int(escolha) not in range(1,61):
        print 'Por favor, escolha um numero entre 1 e 60'

    else:
        print 'Por favor, escolha um numero'

dezenas_escolhidas.sort()
print 'Suas dezenas sao: %02d, %02d, %02d, %02d, %02d, %02d' % (dezenas_escolhidas[0], dezenas_escolhidas[1], dezenas_escolhidas[2],dezenas_escolhidas[3], dezenas_escolhidas[4] ,dezenas_escolhidas[5])

## Preparar desempenho da aposta
quadras = 0
quinas = 0
senas = 0

## Verificar desempenho da aposta
for resultado in resultados:
    resultado = resultado.replace('\n', '')
    resultado = resultado.split('\t')
    del resultado[0]
    ## Contando os acertos em cada resultado
    acertos = 0
    for escolha in dezenas_escolhidas:
        if str(escolha) in resultado:
            acertos += 1
    if acertos == 4:
        quadras += 1
    elif acertos == 5:
        quinas += 1
    elif acertos == 6:
        senas += 1

print 'Seu desempenho foi:'
print '%-10s %d' % ('Quadras: ', quadras)
print '%-10s %d' % ('Quinas: ', quinas)
print '%-10s %d' % ('Senas: ', senas)
    
