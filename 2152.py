for _ in range(int(input())):
    h, m, p = [int(i) for i in input().split()]
    print("{:02d}:{:02d} - A porta {}!".format(h, m, 'abriu' if p == 1 else 'fechou'))
