def depth_first_search(adjacencias, estado_objetivo, estado_inicial):
    pilha = []
    estado_atual = estado_inicial
    expandidos = { estado_atual: None }
    while estado_atual != estado_objetivo:
        for i in range(len(adjacencias[estado_atual])):
            if adjacencias[estado_atual][i] == 1 and i not in expandidos:
                pilha.append(i) # adiciona o indice relativo ao nó
                expandidos[i] = estado_atual
        estado_atual = pilha.pop()
    
    percurso = [ estado_atual ]
    etapa = estado_atual
    while True:
        etapa = expandidos[etapa]
        if etapa == None:
            break
        else:
            percurso.insert(0, etapa)
    return percurso
