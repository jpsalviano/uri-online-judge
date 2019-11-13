t = int(input())

def conversao():
    if c == 'eye':
        return int(0.3*r + 0.59*g + 0.11*b)
    elif c == 'min':
        return int(min([r, g, b]))
    elif c == 'max':
        return int(max([r, g, b]))
    elif c == 'mean':
        return int((r + g + b)/3)

for n in range(1, t+1):
    c = input()
    r, g, b = [int(x) for x in input().split()]
    print('Caso #{}: {}'.format(n, conversao()))
