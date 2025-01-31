def generar_divisores(numero):
    divisores = [i for i in range(1, numero + 1) if numero % i == 0]
    return divisores
numero = 4
divisores = generar_divisores(numero)
print(divisores)