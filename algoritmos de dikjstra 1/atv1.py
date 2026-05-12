grafo = {
    "poster": {
        "violao": 30,
        "bateria": 50
    },
    "violao": {
        "piano": 40
    },
    "bateria": {
        "piano": 20
    },
    "piano": {}
}

custos = {
    "violao": 30,
    "bateria": 50,
    "piano": float("inf")
}

pais = {
    "violao": "poster",
    "bateria": "poster",
    "piano": None,
    "poster": None  
}

processados = []

def ache_no_custo_mais_baixo(custos):
    menor_custo = float("inf")
    menor_no = None
    for no in custos:
        custo = custos[no]
        if custo < menor_custo and no not in processados:
            menor_custo = custo
            menor_no = no
    return menor_no

no = ache_no_custo_mais_baixo(custos)

while no is not None:
    custo = custos[no]
    vizinhos = grafo[no]
    for n in vizinhos:
        novo_custo = custo + vizinhos[n]
        if novo_custo < custos[n]:
            custos[n] = novo_custo
            pais[n] = no
    processados.append(no)
    no = ache_no_custo_mais_baixo(custos)

print("Menor custo até o piano:", custos["piano"])

caminho = []
atual = "piano"

while atual is not None:
    caminho.append(atual)
    atual = pais.get(atual) 

caminho.reverse()

print("Caminho:", caminho)