t = int(input())

def golpe(a, d, l, b):
    if (l % 2 == 0):
        valor_golpe = (a + d)/2 + b
    else:
        valor_golpe = (a + d)/2
    return valor_golpe

for _ in range(t):
    bonus = int(input())
    ad, dd, ld = [int(i) for i in input().split()]
    ag, dg, lg = [int(i) for i in input().split()]
    if golpe(ad, dd, ld, bonus) > golpe(ag, dg, lg, bonus):
        print('Dabriel')
    elif golpe(ag, dg, lg, bonus) > golpe(ad, dd, ld, bonus):
        print('Guarte')
    else:
        print('Empate')
