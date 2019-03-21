A = float(input())
B = float(input())

def average1(a, b):
    a = a * 3.5
    b = b * 7.5
    MEDIA = (a+b)/11
    print('MEDIA = ' + '{:0.5f}'.format(MEDIA))
    return

average1(A, B)
