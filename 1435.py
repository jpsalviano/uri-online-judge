# 1435

while True:
    ordem = int(input())

    if (ordem == 0):
        break

    matriz =  []

    for i in range(ordem):
        linha = []
        for j in range(ordem):
            linha.append(1)
        matriz.append(linha)

    valor = 1           
    cima = 0
    esq = 0
    baixo = ordem - 1
    direita = ordem - 1

    if (ordem % 2 == 0):
        meio = ordem / 2

    else:
        meio = (ordem + 1) / 2


    while (valor <= meio): # linha a linha até chegar a metade da matriz
        i = esq
        while (i <= direita): # esquerda (0) sobe até chegar a direita (ordem - 1)
            matriz[cima][i] = valor
            matriz[baixo][i] = valor
            i+=1

        i = (cima + 1)
        while ( i < baixo):
            matriz[i][esq] = valor
            matriz[i][direita] = valor
            i+=1

        valor+=1
        cima+=1
        baixo-=1
        esq+=1
        direita-=1

    for i in range(ordem):
        tx = ''
        for j in range(ordem):
            tx += " %3d" %matriz[i][j]
        print(tx[1:])
    print("")
