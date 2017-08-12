### -*- coding: cp1252 -*-
#### Exercicio 1
##meu_arquivo = open('texto.txt', 'r')
##texto = meu_arquivo.read()
##meu_arquivo.close()
##
##texto = texto.replace('\n', ' ')
##lista_de_palavras = texto.split(' ')
##lista_de_palavras_unicas = []
##for palavra in lista_de_palavras:
##    if len(palavra) > 4 and palavra not in lista_de_palavras_unicas:
##        lista_de_palavras_unicas.append(palavra)
##
##lista_de_palavras_unicas.sort()
##for palavra_unica in lista_de_palavras_unicas:
##    print palavra_unica
##
#### Exercicio 2
##meu_arquivo = open('Palavras.txt', 'r')
##texto = meu_arquivo.read()
##meu_arquivo.close()
##texto = texto.replace('\n', ' ')
##dicionario = texto.split(' ')
##
##adivinhar_palavra = raw_input('Digite uma palavra para ser adivinhada:\n')
##
##
##respostas = []
##for palavra in dicionario:
##    adicionar = True
##    adivinhar_palavra = adivinhar_palavra.upper()
##    if len(palavra) == len(adivinhar_palavra):
##        for i in range(0, len(adivinhar_palavra)):
##            if adivinhar_palavra[i] == '*':
##                pass
##            elif adivinhar_palavra[i] == palavra[i]:
##                pass
##            else:
##                adicionar = False
##    else:
##        adicionar = False
##
##    if adicionar == True:
##        respostas.append(palavra)
##
##for resposta in respostas:
##    print resposta
##
#### Exercicio 3
##import random
##
##meu_arquivo = open('Palavras.txt', 'r')
##texto = meu_arquivo.read()
##meu_arquivo.close()
##texto = texto.replace('\n', ' ')
##dicionario_base = texto.split(' ')
##dicionario_filtrado = []
##
##for palavra in dicionario_base:
##    if len(palavra) >= 10 and '-' not in palavra:
##        dicionario_filtrado.append(palavra)
##
##palavra_secreta = random.choice(dicionario_filtrado)
##palavra_printada = ''
##asterisco = '*'
##
##for i in range(0, len(palavra_secreta)):
##    esconcer = random.randint(0, 1)
##    if esconcer == 1:
##        palavra_printada += asterisco
##    else:
##        palavra_printada += palavra_secreta[i]
##
##erros = 0
##limite_de_erros = 5
##acerto = False
##
##
##while erros <= limite_de_erros and acerto == False:
##    print 'A palavra a ser descoberta é: ' + palavra_printada
##    print 'Você tem ' + str(limite_de_erros-erros) + ' chances restantes'
##    print 'Escolha uma letra'
##    tentativa = raw_input('').upper()
##    if len(tentativa) == 1:
##        if tentativa in palavra_secreta:
##            nova_palavra_printada = ''
##            for letra in palavra_secreta:
##                if letra == tentativa or letra in palavra_printada:
##                    nova_palavra_printada += letra
##                else:
##                    nova_palavra_printada += asterisco
##            palavra_printada = nova_palavra_printada
##            if asterisco not in palavra_printada:
##                acerto = True
##
##        else:
##            erros = erros + 1
##    else:
##        print 'Por favor, somente uma letra'
##
##if erros > limite_de_erros and acerto == False:
##    print 'Você perdeu!!!'
##
##elif erros <= limite_de_erros and acerto == True:
##    print palavra_printada
##    print 'Parabéns, você acertou.'
##
