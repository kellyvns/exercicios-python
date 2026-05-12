vertices = ["API", "Cache", "Banco"]

arestas = [
    ("API", "Cache", 2),
    ("Cache", "Banco", -5)
]

dist = {
    "API": 0,
    "Cache": 999,
    "Banco": 999
}

for i in range(len(vertices)-1):

    for u, v, peso in arestas:

        if dist[u] + peso < dist[v]:

            dist[v] = dist[u] + peso


print(dist)