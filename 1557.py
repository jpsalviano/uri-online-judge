# 1557

while True:
    ordem = range(int(input()))
    if ordem == range(0):
        break
    matriz = []
    for i in ordem:
        matriz.append([1])

    for linha in ordem:
        if linha > 0:
            matriz[linha][0] = 2 * matriz[linha - 1][0]
        for coluna in ordem[1:]:
            matriz[linha].append(2 * matriz[linha][coluna-1])

    t = len(str(max(matriz[-1])))

    for linha in matriz:
        l = ''
        for numero in linha:
            l += ' {:>{}d}'.format(numero, t)
        print(l[1:])
    print('')
