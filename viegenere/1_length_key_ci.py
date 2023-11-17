from collections import Counter

texto='Hsat aidtzt neap hwtw pvhxqmrmoa triizatktrqt, myi xvt cippwij mh xvxd xtgvczpdkm ltpa ibwlrri ih. Ds xrgipes st pcxxjwrtea mbippamutygt, M hwtrz as’aw ejkatyx dyf xyxtpzxricgs'
texto_letras = texto.replace(" ","").replace( ',',"").replace('’', "").replace('.',"").lower()
print(texto_letras)

# Dividir el crptogramas en n_partes
def dividir_mensaje_longitud_key(message, n_parts):
    if n_parts < 2:
        return [message]  # No se puede dividir en menos de 2 partes

    parts = ["" for _ in range(n_parts)]
    
    for i in range(len(message)):
        part_index = i % n_parts
        parts[part_index] += message[i]
    return parts

# Función que te saca el indice de coincidencia para un criptograma o 
# para un sub-criptograma
def indice_coincidencia(texto):
    num = 0.0
    den = 0.0
    frecuencias = Counter(char for char in texto.lower())
    for val in frecuencias.values():
        i = val
        num += i * (i - 1)
        den += i

    if den == 0.0:
        return 0.0
    else:
        return num / (den * (den - 1))

# Calcular la media de n_sub-critogramas
def calcular_media_ic(texto,n_partes):
    parts = dividir_mensaje_longitud_key(texto,n_partes)
    sum = 0
    for tex in parts:
        sum = indice_coincidencia(tex) + sum
    med = sum / n_partes
    print(f'IC_de_{n_partes}_sub-critogramas: {med}')

############################################################################
print(f'IC_todo_el_texto: {indice_coincidencia(texto_letras)}')

for n_partes in range(2,8):
    calcular_media_ic(texto_letras,n_partes)
############################################################################