import heapq

grafo = {
    "A": {"B": 2},
    "B": {"C": 3},
    "C": {}
}


def dijkstra():

    fila = [(0, "A")]
    visitados = []

    while fila:

        custo, cidade = heapq.heappop(fila)

        if cidade not in visitados:

            visitados.append(cidade)

            print(cidade, custo)

            for vizinho in grafo[cidade]:

                novo = custo + grafo[cidade][vizinho]

                heapq.heappush(fila, (novo, vizinho))


def bellman():

    print("Usando Bellman-Ford")


negativo = False

for cidade in grafo:

    for vizinho in grafo[cidade]:

        if grafo[cidade][vizinho] < 0:
            negativo = True


if negativo:
    bellman()
else:
    dijkstra()