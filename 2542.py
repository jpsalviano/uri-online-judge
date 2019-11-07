def iudioh(carta1, carta2, atributo):
    a, b = carta1[atributo], carta2[atributo]
    if a > b:
        return 1
    elif b > a:
        return 2
    else:
        return 3

while True:
    try:
        n = int(input())
        m, l = [int(x) for x in input().split()]
        m_deck = [[int(x) for x in input().split()] for i in range(m)]
        l_deck = [[int(x) for x in input().split()] for i in range(l)]
        cm, cl = [int(x)-1 for x in input().split()]
        a = int(input())-1
        resultado = iudioh(m_deck[cm], l_deck[cl], a)
        if resultado == 1:
            print('Marcos')
        elif resultado == 2:
            print('Leonardo')
        else:
            print('Empate')
    except EOFError:
        break
