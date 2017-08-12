meu_arquivo = open('Palavras.txt', 'r')
texto = meu_arquivo.read()
meu_arquivo.close()
texto = texto.replace('\n', ' ')
dicionario = texto.split(' ')

adivinhar_palavra = raw_input('Digite uma palavra para ser adivinhada:\n')


respostas = []
for palavra in dicionario:
    adicionar = True
    adivinhar_palavra = adivinhar_palavra.upper()
    if len(palavra) == len(adivinhar_palavra):
        for i in range(0, len(adivinhar_palavra)):
            if adivinhar_palavra[i] == '*':
                pass
            elif adivinhar_palavra[i] == palavra[i]:
                pass
            else:
                adicionar = False
    else:
        adicionar = False

    if adicionar == True:
        respostas.append(palavra)

for resposta in respostas:
    print resposta
