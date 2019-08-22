# 1435

# pega o valor da ordem da matriz, se for 0, encerra o programa
while True:
    ordem = int(input())
    if (ordem == 0):
        break
    
    # cria a matriz numa lista de listas, com todos os elementos de valor 1 
    matriz =  []
    for i in range(ordem):
        matriz.append([])
        for j in range(ordem):
            matriz[i].append(1)

    # valor a ser manipulado, primeira linha de cima e primeira coluna da esquerda
    # com indice 0, ultima linha de baixo e ultima coluna a direita com indice
    # ordem - 1
    valor = 1           
    cima = 0
    esq = 0
    baixo = ordem - 1
    direita = ordem - 1

    # determina a linha/coluna do meio da matriz
    if (ordem % 2 == 0):
        meio = ordem / 2
    else:
        meio = (ordem + 1) / 2

    # mudança dos valores dos elementos para solucionar o problema
    # aumentando em direção ao meio, começando do 1
    while (valor <= meio):
        # define os valores nas linhas de cima e baixo, da esquerda pra direita
        i = esq
        while (i <= direita):
            matriz[cima][i] = valor
            matriz[baixo][i] = valor
            i+=1

        # define os valores nas colunas esquerda e direita, de cima pra baixo
        i = (cima + 1)
        while ( i < baixo):
            matriz[i][esq] = valor
            matriz[i][direita] = valor
            i+=1

        valor+=1    # aumenta conforme se aproxima do meio da matriz
        cima+=1     # aumenta o indice, indo para a linha abaixo da de cima
        baixo-=1    # diminui o indice, indo para linha acima da debaixo
        esq+=1      # aumenta o indice, indo para a coluna à direita
        direita-=1  # diminui o indice, indo para a coluna à esquerda

    # com as listas com os valores corretos, cria string vazia e concatena cada
    # elemento na forma exigida pelo problema (padding 3 alinhado à direita,
    # um espaço em branco separado os elementos, e uma linha em branco separando
    # as matrizes)
    for i in range(ordem):
        tx = ''
        for j in range(ordem):
            tx += ' {:>3d}'.format(matriz[i][j])
        print(tx[1:])
    print('')
