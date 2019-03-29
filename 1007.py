# 1007 - Difference

A = int(input())
B = int(input())
C = int(input())
D = int(input())

def difference(a, b, c, d):
    d1 = a * b
    d2 = c * d
    difference = d1 - d2
    return difference

print('DIFERENCA = ' + str(difference(A, B, C, D)))
