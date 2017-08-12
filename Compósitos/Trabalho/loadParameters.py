def parametersLoad(par): ## Carrega um arquivo correspondente aos parametros
    parameter_list = ['d_unit', 'd', 'Matriz', 'Fibra', 'layers', 'layers_thickness_unit', 'layers_thickness', 'teta_unit', 'teta_interval', 'teta', 'angles'] ## TRADUZIR Parametros a serem extraidos
    filename = 'Parameters/' + par + '.txt' ## Monta o nome do arquivo a ser lido
    file = open(filename, 'r+') ## Abre o arquivo
    lines = file.readlines() ## Separa as linhas do arquivo
    information = [] ## Cria uma lista que ira pegar as informacoes extraidas
    for parameter in parameter_list: ## Para cada parametro dentro da lista de parametros a serem extraidos
        information.append(getParameter(parameter,lines)) ## Adiciona a o parametro a lista com as informacoes
    return information ## Retorna a lista com as informacoes extraidas


def getParameter(parameter,lines): ## Funcao que extrai cada parametro do arquivo
    for i in lines: ## Para cada linha do arquivo
        line = i.split(' ') ## Separa a linha pelos "espaços"
        if parameter == line[0]: ## Se a linha corresponder ao parametro procurado
            return line[2] ## Retorna o valor do parametro
