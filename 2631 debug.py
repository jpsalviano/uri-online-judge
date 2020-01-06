'''
Relações de amizade: (4, 2); (3, 5); (1, 2)
Consultas: a=1 b=4 (S); a=5 b=1 (N)
Lista de checados: sempre começa com o próprio a
1 - percorre a lista de amizades procurando por a
2 - a encontrado: joga o outro item na lista amigos de a, caso não tenha sido
checado anteriormente
'''

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
        print(f'checked = {checked} amigo = {amigo}')
        for amizade in amizades:
            if amigo in amizade:
                outro = amizade[amizade.index(amigo)-1]
                print(f'outro = {outro}')
                if outro == b:
                    return print('S')
                elif outro in checked:
                    pass
                else:
                    amigos_a.append(outro)
    print(f'amigos_a = {amigos_a}')
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
            print(f'consulta: a={a} b={b} in {amizades}')
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
