def contar(texto):
    vocales = 'aeiouAEIOU'
    total = 0
    res = {'vocales': 0, 'consonantes': 0}
    for i in texto:
        if i in vocales:
            res['vocales'] += 1
        else:
            res['consonantes'] += 1
        
    resultado = contar(total)
    return resultado