import heapq
def dijkstra_algorithm(adjacencias, estado_inicial, estado_objetivo):
    min_heap = []
    heapq.heappush(min_heap, (0, estado_inicial))
    expandidos = {}
    expandidos[estado_inicial] = (0, None)
    estado_atual = None
    while min_heap:
        estado_atual = heapq.heappop(min_heap)
        custo_atual, no_atual = estado_atual
        
        if no_atual in expandidos and custo_atual > expandidos[no_atual][0]:
            continue
        
        if no_atual == estado_objetivo:
            break

        for i in range(len(adjacencias[estado_atual[1]])):
            custo_adjacente = adjacencias[estado_atual[1]][i] 
            custo_acumulado = custo_adjacente + estado_atual[0]
                                    # É verdadeiro quando não está em expandidos ou 
                                    # o custo acumulado é menor que o que já está
            if custo_adjacente > 0 and (i not in expandidos or custo_acumulado < expandidos[i][0]):
                heapq.heappush(min_heap, (custo_acumulado, i))
                expandidos[i] = (custo_acumulado, estado_atual)
    if estado_objetivo not in expandidos: 
        return None

    percurso = [ estado_objetivo ]
    etapa = expandidos[estado_objetivo][1]
    while True:
        if etapa == None:
            break
        percurso.insert(0, etapa[1])
        etapa = expandidos[etapa[1]][1]
    return percurso


