A = float(input())
B = float(input())
C = float(input())

def average2(a, b, c):
    a = a * 2.0
    b = b * 3.0
    c = c * 5.0
    MEDIA = (a+b+c)/10
    print('MEDIA = ' + '{:0.1f}'.format(MEDIA))

average2(A, B, C)
