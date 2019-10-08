while True:
    T = int(input())
    if T == 0:
        break
    for _ in range(T):
        n = int(input())
        if n % 2 == 0:
            print((n-1)*2)
        else:
            print((n-1)*2 + 1)
