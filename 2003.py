import sys

for h in sys.stdin.readlines():
    hora, minuto = [int(i) for i in h.strip().split(':')]
    if hora < 7:
        atraso = 0
    elif hora == 7:
        atraso = minuto
    else:
        atraso = 60 * (hora-7) + minuto
    print('Atraso maximo: {}'.format(atraso))
