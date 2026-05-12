import heapq

grafo = {
    "Dummy": {"F1": 0, "F2": 0, "F3": 0, "F4": 0},

    "F1": {"D": 30},
    "F2": {"D": 20},
    "F3": {"D": 15},
    "F4": {"D": 40},

    "D": {}
}

fila = [(0, "Dummy")]

visitados = []
custos = {"Dummy": 0}

while fila:

    custo, cidade = heapq.heappop(fila)

    if cidade not in visitados:

        visitados.append(cidade)

        for vizinho in grafo[cidade]:

            novo = custo + grafo[cidade][vizinho]

            custos[vizinho] = novo

            heapq.heappush(fila, (novo, vizinho))


print("Menor custo:", custos["D"])