def sweeper(matriz, pos_linha, pos_coluna):
    centro = matriz[pos_linha][pos_coluna]
    if centro == 1:
        return '9'
    else:
        sweep = []
        if pos_linha != 0:
            sweep.append(matriz[pos_linha-1][pos_coluna]) #acima
        if pos_linha != n-1:
            sweep.append(matriz[pos_linha+1][pos_coluna]) #abaixo
        if pos_coluna != 0:
            sweep.append(matriz[pos_linha][pos_coluna-1]) #esquerda
        if pos_coluna != m-1:
            sweep.append(matriz[pos_linha][pos_coluna+1]) #direita
        return str(sum(sweep))

while True:
    try:
        n, m = [int(x) for x in input().split()]
        matriz = [[int(x) for x in input().split()] for i in range(n)]
        for i in range(n):
            linha = ''
            for j in range(m):
                linha += sweeper(matriz, i, j)
            print(linha)
    except EOFError:
        break
