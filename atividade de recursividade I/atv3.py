def somaArray(arr):
    if len(arr) == 0:  
        return 0
    return arr[0] + somaArray(arr[1:])

print(somaArray([1, 2, 3, 4]))  