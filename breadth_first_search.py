

def breadth_first_search(adjacencias, estado_inicial, estado_objetivo):
    fila = [estado_inicial]
    estado_atual = fila.pop(0)
    expandidos = { estado_atual: None }
    while estado_atual != estado_objetivo:
        for i in range(len(adjacencias[estado_atual])):
            if adjacencias[estado_atual][i] == 1 and i not in expandidos:
                fila.append(i)
                expandidos[i] = estado_atual
        estado_atual = fila.pop(0)

    percurso = [ estado_atual ]
    etapa = estado_atual
    while True:
        etapa = expandidos[etapa]
        if etapa == None:
            break
        else:
            percurso.append(etapa)
    return percurso

