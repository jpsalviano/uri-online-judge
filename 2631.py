def main():
    while True:
        try:
            #numero de alunos, numero de relacoes de amizade, numero de consultas
            n, m, q = [int(x) for x in input().split()]
            #cria lista vazia amizades
            amizades = list()
            #armazena todas as m relacoes de amizade em nested lists em amizades
            for _ in range(m):
                x, y = [int(x) for x in input().split()]
                amizades.append([x, y])
            #q consultas: a e b tem relacao direta de amizade?
            for _ in range(q):
                a, b = [int(x) for x in input().split()]
                sao_amigos_diretos(a, b, amizades)
        except EOFError:
            break


def sao_amigos_diretos(pessoa1, pessoa2, lista_de_amizades):
    #procura relacao direta entre 2 pessoas numa lista
    #args: int(pessoa1), int(pessoa2), list(lista_de_amizades)
    amigos, checados = list(), [pessoa1]
    for amizade in lista_de_amizades:
        if pessoa1 in amizade:
            outro = amizade[amizade.index(pessoa1)-1]
            if outro == pessoa2:
                return print('S')
            elif outro in checados:
                continue
            else:
                amigos.append(outro)
    sao_amigos_indiretos(amigos, checados, lista_de_amizades,pessoa2)


def sao_amigos_indiretos(amigos, checados, lista_de_amizades, pessoa2):
    #procura recursivamente relacao indireta entre pessoa1 e pessoa2
    #args: list(amigos), list(checados), int(pessoa2)
    for a in amigos:
        checados.append(a)
        amigos.remove(a)
        for amizade in lista_de_amizades:
            if a in amizade:
                outro = amizade[amizade.index(a)-1]
                if outro == pessoa2:
                    return print('S')
                elif outro in checados:
                    continue
                else:
                    amigos.append(outro)
    if amigos: #se nao e lista vazia
        sao_amigos_indiretos(amigos, checados, lista_de_amizades, pessoa2)
    else:
        return print('N')


main()

'''
5 3 3
4 2
3 5
1 2
1 4
5 1
2 4
'''
