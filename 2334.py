while True:
    p = int(input())
    if p == -1:
        break
    print('{}'.format(p-1 if p > 0 else 0))
