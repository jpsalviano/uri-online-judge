import sys

entrada = sys.stdin.readlines()
l = 0
linhas = len(entrada)

def distancia(lista):
    ash = []
    poke = []
    for l, linha in enumerate(lista):
        if '1' in linha:
            ash.append(l)
            ash.append(linha.index('1'))
    for l, linha in enumerate(lista):
        if '2' in linha:
            poke.append(l)
            poke.append(linha.index('2'))
    diferenca = abs(ash[0] - poke[0]) + abs(ash[1] - poke[1])
    return diferenca

while l < linhas:
    n, m = [int(x) for x in entrada[l].split()]
    cidade = []
    for i in range(l+1, l+1+n):
        cidade.append(entrada[i].strip().split())
    print(distancia(cidade))
    l += n + 1
