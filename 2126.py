import sys

entrada = sys.stdin.readlines()

for caso, i in enumerate(range(0, len(entrada), 2), 1):
    q = entrada[i+1].strip().count(entrada[i].strip())
    p = entrada[i+1].strip().rfind(entrada[i].strip()) + 1
    if q == 0:
        print('Caso #{}:\nNao existe subsequencia\n'.format(caso))
    else:
        print('Caso #{}:\nQtd.Subsequencias: {}\nPos: {}\n'.format(caso,q,p))
