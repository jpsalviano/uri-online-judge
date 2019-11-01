def ispossible(a, b, c):
    #condições de existência do triângulo
    if abs(b - c) < a < (b + c):
        if abs(a - c) < b < (a + c):
            if abs(a - b) < c < (a + b):
                return triang_type(a, b, c)
    else:
        return 'Invalido'

def triang_type(a, b, c):
    #equilatero
    if (a == b == c):
        return 'Valido-Equilatero\nRetangulo: N'
    #retangulo
    l = [a, b, c]
    hip = max(l)
    cat = l.remove(hip)
    r = 'S' if hip**2 == l[0]**2 + l[1]**2 else 'N'
    #isosceles
    if (a == b and a != c) or (b == c and b != a) or (c == a and c != b):
        return 'Valido-Isoceles\nRetangulo: {}'.format(r)
    #escaleno
    if (a != b and a != c and b != c):
        return 'Valido-Escaleno\nRetangulo: {}'.format(r)

def main():
    a, b, c = [int(x) for x in input().split()]
    print(ispossible(a, b, c))

main()
