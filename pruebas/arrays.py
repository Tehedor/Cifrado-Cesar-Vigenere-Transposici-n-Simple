from itertools import permutations


def permutaciones_rotativas():
    arr = [1, 2, 3, 4, 5, 6]
    n = len(arr)
    permutaciones = list(permutations(arr))
    
    for p in permutaciones:
       a= yield list(p)
       

# Ejemplo de uso:
arr = [1, 2, 3, 4, 5, 6]

generador = permutaciones_rotativas()

# for permutacion in permutaciones_rotativas(arr):
#     print(permutacion)

    # print(a)

for permutacion in generador:
    print(permutacion)