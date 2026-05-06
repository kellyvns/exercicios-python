rotas = {
    "Twin Peaks": ["Stop A", "Stop B"],
    "Stop A": ["Stop C"],
    "Stop B": ["Stop C", "Stop D"],
    "Stop C": ["Golden Gate Bridge"],
    "Stop D": [],
    "Golden Gate Bridge": []
}

def menor_caminho(inicio, destino):
    fila = []
    fila.append((inicio, 0)) 
    visitados = []

    while fila:
        atual, dist = fila.pop(0)

        if atual == destino:
            print("etapas:", dist)
            return

        if atual not in visitados:
            visitados.append(atual)

            for vizinho in rotas[atual]:
                fila.append((vizinho, dist + 1))

    print("Caminho não encontrado")


menor_caminho("Twin Peaks", "Golden Gate Bridge")