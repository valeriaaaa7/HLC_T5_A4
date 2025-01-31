def palabras(lista):
    diccionario = {palabra: len(palabra) for palabra in lista}
    print("Diccionario con longitud: "+str(diccionario))

lista = ['camila', 'valeria', 'seguridad']
print(+str(lista))
palabras(lista)