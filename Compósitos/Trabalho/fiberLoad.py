def fiberLoad(fiber): ## Carrega um arquivo correspondente a um tipo de fibra
    parameter_list = ['E1', 'E2', 'G12', 'v12', 'Xt', 'Xc', 'Yt', 'Yc', 'S12'] ## Parametros a serem extraidos
    filename = 'Fibers/' + fiber + '.txt' ## Monta o nome do arquivo a ser lido
    fiber = open(filename, 'r+') ## Abre o arquivo
    lines = fiber.readlines() ## Separa as linhas do arquivo
    information = [] ## Cria uma lista que ira pegar as informacoes extraidas
    for parameter in parameter_list: ## Para cada parametro dentro da lista de parametros a serem extraidos
        information.append(getParameter(parameter,lines)) ## Adiciona a o parametro a lista com as informacoes
    return information ## Retorna a lista com as informacoes extraidas


def getParameter(parameter,lines): ## Funcao que extrai cada parametro do arquivo
    for i in lines: ## Para cada linha do arquivo
        line = i.split(' ') ## Separa a linha pelos "espaços"
        if parameter == line[0]: ## Se a linha corresponder ao parametro procurado
            return float(line[2]) ## Retorna o valor do parametro

