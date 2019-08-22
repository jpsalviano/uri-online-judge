# 1478

while True:
    # pega a ordem da matriz, se for 0 finaliza o programa
    N = int(input())
    if (N == 0):
        break
    
    # cria a matriz de ordem N com 1 no lugar de todos os elementos
    matriz = []
    for i in range(N):
        matriz.append([])
        for j in range(N):
            matriz[i].append(1)

    # altera os valores da primeira linha (ordem crescente a partir do 1)
    for col in range(1,N):
        matriz[0][col] = matriz[0][col-1] + 1

    # altera os valores do restante da primeira coluna
    for line in range(1, N):
        matriz[line][0] = matriz[0][line]

    # alterar os demais valores, com base no primeiro valor
    for line in range(1, N):
        decrease = True
        col = 1
        # diminui até chegar em 1
        while decrease:
            matriz[line][col] = matriz[line][col-1] - 1
            if matriz[line][col] == 1:
                decrease = False
            col += 1
        # chegando em 1, aumenta ate a ultima coluna
        for col in range(col, N):
            matriz[line][col] = matriz[line][col-1] + 1

    # printa a matriz de acordo as regras do problema: padding 3, numero alinhado
    # a direita, um espaço em branco apos o numero, uma linha em branco apos
    # cada matriz
    for line in range(N):
        linha = ''
        for col in range(N):
            linha += ' {:>3d}'.format(matriz[line][col])
        print(linha[1:])
    print()
