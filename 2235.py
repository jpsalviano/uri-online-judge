a, b, c = [int(x) for x in input().split()]

if a == b or a == c or b == c or (a + b) == c or (a + c) == b or (b + c) == a:
    print('S')
else:
    print('N')
