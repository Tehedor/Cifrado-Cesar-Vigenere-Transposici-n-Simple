texto='Hsat aidtzt neap hwtw pvhxqmrmoa triizatktrqt, myi xvt cippwij mh xvxd xtgvczpdkm ltpa ibwlrri ih. Ds xrgipes st pcxxjwrtea mbippamutygt, M hwtrz as’aw ejkatyx dyf xyxtpzxricgs'
texto_sin_espacios = texto.replace(" ","")

# Función que crea la matriz vigenere
def crear_matriz_vigenere():
    alfabeto = 'abcdefghijklmnopqrstuvwxyz' 
    matriz = [[0] * 26 for _ in range(26)]

    for fila in range(26):
        for columna in range(26):
            letra = (fila + columna) % 26
            matriz[fila][columna] = alfabeto[letra]

    return matriz

# Función la cual a partir de una letra te saca su posición en el abcdario
def posicion_en_abc(letra):
    letra = letra.lower()  
    if 'a' <= letra <= 'z':
        return ord(letra) - ord('a')
    else:
        return None  

# Función que descifra el mensaje a partir de un texto cifrado y su calve
def mensaje_descifrado(texto, clave):
    mensaje_descifrado = ""
    matriz_vigenere = crear_matriz_vigenere()
    texto = texto.lower()
    i=0
    for letra in texto:
        if letra == " " or letra == ",":
            mensaje_descifrado += letra
        else:
            n = clave[i % len(clave)]
            for j,l in enumerate(matriz_vigenere[posicion_en_abc(n)]):
                if l == letra:
                    columna = j
                    mensaje_descifrado += matriz_vigenere[0][columna]
                    i += 1
                    break

    return mensaje_descifrado

############################################################################

clave='people'
print(texto_sin_espacios)
mesaje_descifrado = mensaje_descifrado(texto,clave)
print(mesaje_descifrado)

############################################################################