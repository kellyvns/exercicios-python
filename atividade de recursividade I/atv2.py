def potencia(base, expoente):
    if expoente < 0:
        raise ValueError("O expoente deve ser não negativo")
    if expoente == 0:  
        return 1
    return base * potencia(base, expoente - 1)

print(potencia(2, 4))  