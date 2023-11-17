from itertools import permutations

# Crea todas las posibles combinaciones de columnas para un numero de columnas dado
def permutaciones_rotativas(num_columnas):
    arr = list(range(1, num_columnas + 1)) 
    permutaciones = list(permutations(arr))
    
    for p in permutaciones:
       yield list(p)
    
    return permutaciones

def descifrar_mensaje(texto, num_columnas, column_order):
    for i in range(len(column_order)):
        column_order[i] -= 1    
    
    # Filas de la matriz que va a ser rellenada
    num_filas = (len(texto) + num_columnas - 1) // num_columnas

    # Calculamos cuantos espacios en blanco va a haber en la ultima fila, ya que si rellenamos
    # estos espacios cuando rellenemos las columnas no podremos descifrar el texto ya
    # que se debe rellar de la misma forma que se hizo al cifrar el texto
    num_celdas_matriz = num_filas*num_columnas
    num_celdas_vacias = num_celdas_matriz - len(texto)
    elementos_1 = num_columnas - num_celdas_vacias
    ultima_fila = [1] * elementos_1 + [0] * (num_columnas - elementos_1)  
 
    matriz = [['.' for _ in range(num_columnas)] for _ in range(num_filas)]
    orden_letras = 0
    # Rellenamos la matriz en funcion de columna_orden
    for columna in column_order:
        for fila in range(num_filas):
            if not (fila == num_filas-1 and ultima_fila[columna]==0):
                if orden_letras < len(texto):
                    matriz[fila][columna] = texto[orden_letras]
                    orden_letras += 1 
    
    mensaje = ""

    for fila in matriz:
        for letra in fila:
            if (letra != ".") and (letra != ","):
                mensaje += letra

    return mensaje

############################################################################

texto = "THLAULDTOHINHEUBETTWOHWPTSREGCMGETNTSUAGEEIISIDTLATCOIFTERRONMIDSOHKNFSBPEUTOHOTAILTDETGT"

# num_columnas = 4
# generador = permutaciones_rotativas(num_columnas)

# with open("transposicion_4_columnas.txt", "w") as archivo:
#     for permutacion in generador:
#         # print(permutacion)
#         mensaje = descifrar_mensaje(texto, num_columnas, permutacion)
#         archivo.write(f" {permutacion} es: {mensaje}\n")


# num_columnas = 5
# generador = permutaciones_rotativas(num_columnas)

# with open("transposicion_5_columnas.txt", "w") as archivo:
#     for permutacion in generador:
#         # print(permutacion)
#         mensaje = descifrar_mensaje(texto, num_columnas, permutacion)
#         archivo.write(f" {permutacion} es: {mensaje}\n")

num_columnas = 6
generador = permutaciones_rotativas(num_columnas)

with open("transposicion_6_columnas.txt", "w") as archivo:
    for permutacion in generador:
        mensaje = descifrar_mensaje(texto, num_columnas, permutacion)
        archivo.write(f" {permutacion} es: {mensaje}\n")

############################################################################
