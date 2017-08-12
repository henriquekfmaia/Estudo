meu_arquivo = open('texto.txt', 'r')
texto = meu_arquivo.read()
meu_arquivo.close()

texto = texto.replace('\n', ' ')
lista_de_palavras = texto.split(' ')
lista_de_palavras_unicas = []
for palavra in lista_de_palavras:
    if len(palavra) > 4 and palavra not in lista_de_palavras_unicas:
        lista_de_palavras_unicas.append(palavra)

lista_de_palavras_unicas.sort()
for palavra_unica in lista_de_palavras_unicas:
    print palavra_unica
