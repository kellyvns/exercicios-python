import heapq

grafo = {
    "Manhuaçu": {"João Monlevade": 180, "Ouro Preto": 120},
    "João Monlevade": {"Belo Horizonte": 90},
    "Ouro Preto": {"Belo Horizonte": 100},
    "Belo Horizonte": {"Mineirão": 20},
    "Mineirão": {}
}

def dijkstra(inicio, fim):

    fila = [(0, inicio, [])]
    visitados = []

    while fila:

        custo, cidade, caminho = heapq.heappop(fila)

        if cidade not in visitados:

            visitados.append(cidade)

            caminho = caminho + [cidade]

            if cidade == fim:
                return custo, caminho

            for vizinho in grafo[cidade]:

                novo_custo = custo + grafo[cidade][vizinho]

                heapq.heappush(fila, (novo_custo, vizinho, caminho))


tempo, rota = dijkstra("Manhuaçu", "Mineirão")

print("Tempo:", tempo)
print("Rota:", rota)