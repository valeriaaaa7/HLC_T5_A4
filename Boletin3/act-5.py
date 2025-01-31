def frecuenciaPalabras():
    frase = "sistemas sistemas microinfoematicos y redes"
    palabras = frase.split()
    frecuencia = {}
    
    for palabra in palabras:
        if palabra in frecuencia:
            frecuencia[palabra] += 1
        else:
            frecuencia[palabra] = 1

    return frecuencia
print(frecuenciaPalabras())