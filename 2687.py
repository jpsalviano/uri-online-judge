# 2687

# Depth-first search

# 1 procura pelos 0 fora do perimetro de 1 (linha 0 e -1, coluna 0 e -1)
# 2 guarda a quantidade de 0 fora do perimetro de 1
# 3 output: ((L x L) - quantidade de 0 fora do perimetro de 1)/2

# cria uma lista de marcacao marked = []
# busca na primeira row completa, depois desce checando o primeiro e ultimo itens ate a ultima row completa
# for i, row in enumerate(grid) -> for j, col in enumerate(row)
# -> if i != 0 or l-1 -> if j != 0 or l-1 -> continue
# sobre o elemento: if == 0 && if not in marked
# marca: marked.append (row, col)
# cria o stack com o ultimo item da lista de marcacao = [marked[-1]]
###recursive:
# while True:
# if len(stack) == 0, break
# e = stack[-1] > procura ao redor de e -> for n, next in enumerate(grid[r-1][c], grid[r][c+1], grid[r+1][c], grid[r][c-1])
# if next nao existe, esta marcado ou == 1 AND n == 3 -> del stack[-1]
# elif next nao existe, esta marcado ou == 1, continue
# else, marked.append(next), stack.append(next), break


q = int(input())  #quantidade de bacterias

for _ in range(q):
    l = int(input())  #length - largura e altura do grid
    grid = []  #cria o grid vazio
    for _ in range(l):  #preenche com l inputs
        row = input().split()
        grid.append(row)
    marked = []  #lista de elementos marcados
    for i_row, row in enumerate(grid):  #percorre todas rows
        for i_col, col in enumerate(row):  #percorre todas cols
            if (i_row != 0 or l-1) and (i_col != 0 or l-1):  #ignora rows e cols que nao sejam a primeira (0) ou a ultima (-1)
                continue
            e_row, e_col, e_val = (i_row, i_col, int(grid[i_row][i_col]))  #elemento (x, y, v = 0 ou 1)
            if (e_val == 0) and (e_row, e_col) not in marked:  #se elemento for zero e nao estiver marcado
                marked.append((e_row, e_col))  #marca o item
                stack = [marked[-1]]  #cria stack com o ultimo item da lista
                while True:  #entra na busca dfs recursiva
                    if len(stack) == 0:  #para quando o stack tiver zerado
                        break
                    #up, right, bottom and left neighbours in list neighbors
                    neighbors_coordinates = [ (e_row-1, e_col), (e_row, e_col+1), (e_row+1, e_col), (e_row, e_col-1) ]
                    #cria lista de vizinhos excluindo os impossiveis (index fora do grid)
                    neighbors = [n for n in neighbors_coordinates if 0 <= n[0] <= l-1 and 0 <= n[1] <= l-1]
                    for i_n, n in enumerate(neighbors):  #checa cada um dos vizinhos possiveis
                        n_row, n_col, n_val = (n[0], n[1], int(grid[n_row][n_col]))  #guarda row x col e value (0 ou 1)
                        if (n_val == 1) or (n_row, n_col) in marked:  #se for 1 ou tiver marcado
                            if i_n == (len(neighbors) - 1): #checa se é o ultimo neighbor...
                                del stack[-1]  #caso seja: deleta o ultimo item do stack
                            continue  #caso nao seja: simplesmente checa o proximo vizinho (ou encerra o loop caso seja o ultimo)
                        else:  #caso nao esteja marcado nem seja 1
                            mark.append((n_row, n_col))  #marca
                            stack.append((n_row, n_col)) #joga no stack como ultimo item
                            break  #encerra o for loop e volta pro while loop pra checar o ultimo item do stack
    print( (l**2 - len(marked)) / 2 )  #printa a quantidade de elementos - marcados / 2