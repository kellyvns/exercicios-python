vertices = ["A", "B", "C"]

arestas = [
    ("A", "B", 1),
    ("B", "C", -2),
    ("C", "A", -2)
]

dist = {}

for v in vertices:
    dist[v] = 999

dist["A"] = 0


for i in range(len(vertices)-1):

    for u, v, peso in arestas:

        if dist[u] + peso < dist[v]:

            dist[v] = dist[u] + peso


ciclo = False

for u, v, peso in arestas:

    if dist[u] + peso < dist[v]:
        ciclo = True

if ciclo:
    print("Existe ciclo negativo")
else:
    print("Não existe ciclo negativo")