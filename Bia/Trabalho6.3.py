# -*- coding: cp1252 -*-
import random

meu_arquivo = open('Palavras.txt', 'r')
texto = meu_arquivo.read()
meu_arquivo.close()
texto = texto.replace('\n', ' ')
dicionario_base = texto.split(' ')
dicionario_filtrado = []

for palavra in dicionario_base:
    if len(palavra) >= 10 and '-' not in palavra:
        dicionario_filtrado.append(palavra)

palavra_secreta = random.choice(dicionario_filtrado)
palavra_printada = ''
asterisco = '*'

for i in range(0, len(palavra_secreta)):
    esconcer = random.randint(0, 1)
    if esconcer == 1:
        palavra_printada += asterisco
    else:
        palavra_printada += palavra_secreta[i]

erros = 0
limite_de_erros = 5
acerto = False


while erros <= limite_de_erros and acerto == False:
    print 'A palavra a ser descoberta é: ' + palavra_printada
    print 'Você tem ' + str(limite_de_erros-erros) + ' chances restantes'
    print 'Escolha uma letra'
    tentativa = raw_input('').upper()
    if len(tentativa) == 1:
        if tentativa in palavra_secreta:
            nova_palavra_printada = ''
            for letra in palavra_secreta:
                if letra == tentativa or letra in palavra_printada:
                    nova_palavra_printada += letra
                else:
                    nova_palavra_printada += asterisco
            palavra_printada = nova_palavra_printada
            if asterisco not in palavra_printada:
                acerto = True

        else:
            erros = erros + 1
    else:
        print 'Por favor, somente uma letra'

if erros > limite_de_erros and acerto == False:
    print 'Você perdeu!!!'

elif erros <= limite_de_erros and acerto == True:
    print palavra_printada
    print 'Parabéns, você acertou.'

