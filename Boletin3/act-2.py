def quitarDuplicados(palabras):
    return list(set(palabras))
entrada = ['hola', 'mundo', 'hola', 'python', 'mundo']
salida = quitarDuplicados(entrada)
print(salida)