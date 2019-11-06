import sys

entrada = sys.stdin.readlines()
e = 0

while e < len(entrada):
    c, n = [int(x) for x in entrada[e].split()]
    str1 = entrada[e+1].strip() + entrada[e+1].strip().lower()
    str2 = entrada[e+2].strip() + entrada[e+2].strip().lower()
    cifra = str.maketrans(str1+str2, str2+str1)
    print(cifra)
    for i in range(e+3, e+3+n):
        entrada[i] = entrada[i].translate(cifra)
        print(entrada[i], end='')
    print()
    e += 3 + n
