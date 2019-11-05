alimentos_vitc = {'suco de laranja': 120, 'morango fresco': 85,
                  'mamao': 85, 'goiaba vermelha': 70, 'manga': 56,
                  'laranja': 50, 'brocolis': 34}

while True:
    t = int(input())
    if t == 0:
        break
    consumo = 0
    for _ in range(t):
        q, *a = [x for x in input().split()]
        consumo += int(q) * alimentos_vitc[' '.join(a)]
    if consumo > 130:
        print('Menos {} mg'.format(consumo - 130))
    elif consumo < 110:
        print('Mais {} mg'.format(110 - consumo))
    else:
        print('{} mg'.format(consumo))
