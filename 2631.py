def friends(a):
    checked.append(a) # joga na lista de checados
    for amizade in amizades:
        if a in amizade:
            outro = amizade[amizade.index(a)-1]
            if outro == b:
                return print('S')
            elif outro in checked:
                pass
            else:
                amigos_a.append(outro)
    friends_recursive()

def friends_recursive():
    for amigo in amigos_a:
        checked.append(amigo)
        amigos_a.remove(amigo)
        for amizade in amizades:
            if amigo in amizade:
                outro = amizade[amizade.index(amigo)-1]
                if outro == b:
                    return print('S')
                elif outro in checked:
                    pass
                else:
                    amigos_a.append(outro)
    if len(amigos_a) == 0:
        return print('N')
    else:
        friends_recursive()

while True:
    try:
        n, m, q = [int(x) for x in input().split()]
        amizades = list()
        for _ in range(m):
            x, y = [int(x) for x in input().split()]
            amizades.append([x, y])
        for _ in range(q):
            a, b = [int(x) for x in input().split()]
            amigos_a = []
            checked = []
            friends(a)
    except EOFError:
        break


'''
5 3 3
4 2
3 5
1 2
1 4
5 1
2 4
'''
