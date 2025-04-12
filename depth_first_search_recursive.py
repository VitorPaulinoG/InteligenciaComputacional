

def depth_first_search(adjacencias, obj, atual, expandidos = set()):
    # caso base
    if atual == obj:
        return [atual]
    
    expandidos.add(atual)
    
    for i in range(len(adjacencias[atual])):
        if adjacencias[atual][i] == 1 and i not in expandidos:
            result = depth_first_search(adjacencias, obj, i, expandidos)
            if result:
                return [atual] + result
            
    return []