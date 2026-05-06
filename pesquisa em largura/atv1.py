grafo = {
    "voce": ["alice", "bob", "claire"],
    "alice": ["peggy"],
    "bob": ["anuj", "peggy"],
    "claire": ["thom", "jonny"],
    "anuj": [],
    "peggy": [],
    "thom": [],
    "jonny": []
}

def busca_vendedor():
    fila = []
    fila += grafo["voce"]  
    verificados = []

    while fila:
        pessoa = fila.pop(0)  

        if pessoa not in verificados:
            if pessoa[-1] == "m": 
                print(pessoa, "é o vendedor de mangas")
                return
            else:
                fila += grafo[pessoa]
                verificados.append(pessoa)

    print("Vendedor não encontrado")


busca_vendedor()