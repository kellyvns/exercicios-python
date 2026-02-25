def maiorElemento(arr):
    if len(arr) == 0:
        raise ValueError("O array não pode ser vazio")
    if len(arr) == 1:  
        return arr[0]
    
    maior_do_resto = maiorElemento(arr[1:])
    return arr[0] if arr[0] > maior_do_resto else maior_do_resto

print(maiorElemento([3, 7, 2, 9, 5])) 