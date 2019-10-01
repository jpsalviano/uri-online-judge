for _ in range(int(input())):
    p1 = input()
    p2 = input()
    if p1 == p2 == 'ataque':
        print('Aniquilacao mutua')
    elif p1 == p2 == 'papel':
        print('Ambos venceram')
    elif p1 == p2 == 'pedra':
        print('Sem ganhador')
    elif p1 == 'ataque':
        print('Jogador 1 venceu')
    elif p2 == 'ataque':
        print('Jogador 2 venceu')
    elif p1 == 'pedra':
        print('Jogador 1 venceu')
    else:
        print('Jogador 2 venceu')
