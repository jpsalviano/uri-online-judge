while True:
    try:
        n = int(input())
        votos = [int(x) for x in input().split()]
        if (sum(votos)/n >= 2/3):
            print('impeachment')
        else:
            print('acusacao arquivada')
    except EOFError:
        break
