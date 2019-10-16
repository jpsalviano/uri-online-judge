# tentei procurando o 42: time limit exceeded
# este é procurando 7, 7, 7: time limit exceeded também
# acredito que a solução só passa em c++

#terreno
n, m = [int(i) for i in input().split()]
terreno = list()
for _ in range(n):
    terreno.append([int(i) for i in input().split()])

def find777(linha):
    # procura dentro de uma lista a sequencia 7, 7, 7
    # retorna o index do primeiro 7
    return [int(i) for i in range(len(linha)-2) if linha[i:i+3] == [7, 7, 7]]

def find_pattern():
    if terreno[l+1][loc:loc+3] == [7, 42, 7] and terreno[l+2][loc:loc+3] == [7, 7, 7]:
        return True

#coordenadas x, y
c = [0, 0]
#procura 7, 7, 7 em cada linha, até a antepenúltima inclusive
for l, linha in enumerate(terreno[0:-2]):
    locations = find777(linha)
    for loc in locations:
        if find_pattern():
            c = [l+2, loc+2]
            break

print(c[0], c[1])
