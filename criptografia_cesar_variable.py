def cifrado_cesar_variable(texto, desplazamientos):
    alfabeto = 'abcdefghijklmnopqrstuvwxyz'
    alfabeto_may = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    
    texto_descifrado = ''

    for i in range(len(texto)):
        if texto[i] in alfabeto:  
            indice = (alfabeto.index(texto[i]) + desplazamientos[i % len(desplazamientos)]) % len(alfabeto) 
            texto_descifrado += alfabeto[indice]
        elif texto[i] in alfabeto_may:
            indice = (alfabeto_may.index(texto[i]) + desplazamientos[i % len(desplazamientos)]) % len(alfabeto_may)
            texto_descifrado += alfabeto_may[indice]
        else:
            texto_descifrado += texto[i]

    return texto_descifrado

texto = 'Fj lckyamnadlrxjx yb volbx vub zon dhj lonmccxh xn rhoiagjnrwj'

############################################################################

# # [i]
with open("cesar_variable_[i].txt","w") as archivo:
    for i in range(27):
        desplazamientos = [i]
        mensaje_descifrado_ciclo_1 = cifrado_cesar_variable(texto, desplazamientos)
        archivo.write(f"numero de desplazamientos {desplazamientos} es: {mensaje_descifrado_ciclo_1}\n")

# [i,j]
# with open("cesar_variable_[i,j].txt","w") as archivo:
#     for i in range(27):
#         for j in range(27):
#             desplazamientos = [i,j]
#             mensaje_descifrado_ciclo_1 = cifrado_cesar_variable(texto, desplazamientos)
#             archivo.write(f"numero de desplazamientos  {desplazamientos} es: {mensaje_descifrado_ciclo_1}\n")

############################################################################



