import sys

entrada = sys.stdin.readlines()
e = 0

while e < len(entrada):
    c, n = [int(x) for x in entrada[e].split()]
    keys = entrada[e+1].strip()
    values = entrada[e+2].strip()
    cifra = dict(zip(keys, values))
    cifra.update(dict(zip(values, keys)))
    for i in range(e+3, e+3+n):
        for z, l in enumerate(entrada[i]):
            if l.upper() in cifra:
                if l.isupper():
                    entrada[i] = entrada[i][:z] + entrada[i][z:].replace(l, cifra[l.upper()], 1)
                else:
                    entrada[i] = entrada[i][:z] + entrada[i][z:].replace(l, cifra[l.upper()].lower(), 1)
        print(entrada[i], end='')
    print()
    e += 3 + n
