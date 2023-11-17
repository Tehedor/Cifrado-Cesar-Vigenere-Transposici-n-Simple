from collections import Counter

texto='Hsat aidtzt neap hwtw pvhxqmrmoa triizatktrqt, myi xvt cippwij mh xvxd xtgvczpdkm ltpa ibwlrri ih. Ds xrgipes st pcxxjwrtea mbippamutygt, M hwtrz as’aw ejkatyx dyf xyxtpzxricgs'
texto_sin_espacios = texto.replace(" ","").replace( ',',"").replace('’', "").replace('.',"")

# Función que saca un array con n letras más frecuentes
def letras_comunes(numero):
    # Frecuencia de las letras en inglés
    english_letter_frequency = {
        'a': 0.082, 'b': 0.015, 'c': 0.028, 'd': 0.043, 'e': 0.127,
        'f': 0.022, 'g': 0.020, 'h': 0.061, 'i': 0.070, 'j': 0.0015,
        'k': 0.0077, 'l': 0.040, 'm': 0.024, 'n': 0.067, 'o': 0.075,
        'p': 0.019, 'q': 0.00095, 'r': 0.060, 's': 0.063, 't': 0.091,
        'u': 0.028, 'v': 0.0098, 'w': 0.024, 'x': 0.0015, 'y': 0.020,
        'z': 0.00074
    }
    frecuencias_ordenadas = sorted(english_letter_frequency.items(), key=lambda x: x[1], reverse=True)
    letras_comunes = [letra for letra, frecuencia in frecuencias_ordenadas[:numero]]
    return letras_comunes

# Dividir el texto en n sub-criptogramas
def dividir_mensaje_longitud_key(message, num_parts):
    if num_parts < 2:
        return [message]  # No se puede dividir en menos de 2 partes

    parts = ["" for _ in range(num_parts)]
    
    for i in range(len(message)):
        part_index = i % num_parts
        parts[part_index] += message[i]
    return parts

# Cuenta el numero de veces que aparece una letra
def count_letters(text):
    letter_count = {}
    for letter in text:
        if letter.isalpha():  
            letter = letter.lower()  
            if letter in letter_count:
                letter_count[letter] += 1
            else:
                letter_count[letter] = 1
    letter_count = dict(sorted(letter_count.items(), key=lambda item: item[1], reverse=True))
    return letter_count
    
# Mira la distancia entre dos letras
def distancia_entre_letras(letra1, letra2):
    letra1 = letra1.lower()  # Convierte a minúscula para manejar mayúsculas y minúsculas
    letra2 = letra2.lower()
    abc = 'abcdefghijklmnopqrstuvwxyz'
    
    if letra1 in abc and letra2 in abc:
        indice_letra1 = abc.index(letra1)
        indice_letra2 = abc.index(letra2)
        distancia = (indice_letra2 - indice_letra1) % 26
        return distancia
    else:
        return None 

# Da la letra en función de la posicion en la que se encuentre
def letra_dando_num(num):
    abc='abcdefghijklmnopqrstuvwxyz'
    return abc[num]

# Te da el número o númoers más comunes de una lista
def numeros_mas_comunes(lista):
    contador = Counter(lista)
    maxima_frecuencia = max(contador.values())
    numeros_comunes = [numero for numero, frecuencia in contador.items() if frecuencia == maxima_frecuencia]
    return numeros_comunes


# Nos saca la letra que es más común
def letra (frecuencias,letra):
    distancias_0 = []
    for letra2, cantidad in frecuencias.items():
        if cantidad > 1:
            for letra1 in letra:
                distancia = distancia_entre_letras(letra1, letra2)
                distancias_0.append(distancia)

    posicion = numeros_mas_comunes(distancias_0)
    letras =[]
    for value in posicion:
        letras.append(letra_dando_num(value))
    
    return letras




############################################################################

n_partes = 6

texto_dividido = dividir_mensaje_longitud_key(texto_sin_espacios,n_partes)

n = len(texto_dividido)  # Obtener la longitud de texto_dividido
frecuencias = [count_letters(texto_dividido[i]) for i in range(n)]


n_letras = 12
for i in range(3,n_letras):
    letras=letras_comunes(i)
    # print(letras)
    clave =[]
    for j in range(0,6):
        # letra(frecuencias[j],letras) 
        clave.append(letra(frecuencias[j],letras) ) 
        
    # print(clave)
    print(f'comparando {letras} nos sale la clave:{clave}')

############################################################################
