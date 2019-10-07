import sys

dias_no_mes = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def dias_ate_natal(m, d):
    dias = 0
    if (m < 11):
        dias += (dias_no_mes[m-1]-d) + (25)
        for i in dias_no_mes[m:11]:
            dias += i
    elif (m == 11):
        dias += (dias_no_mes[m-1]-d) + (25)
    else:
        dias += (25 - d)
    return dias

for dia in sys.stdin.readlines():
    m, d = map(int, dia.strip().split())
    if (m == 12) and (d == 25):
        print('E natal!')
    elif (m == 12) and (d == 24):
        print('E vespera de natal!')
    elif (m == 12) and (d > 25):
        print('Ja passou!')
    else:
        print('Faltam {} dias para o natal!'.format(dias_ate_natal(m, d)))
