# Simple Sort - 1042

a, b, c = [int(i) for i in input().split()]
abc = [a, b, c]
abc.sort()
for i in abc:
    print(i)
print('')
for i in [a, b, c]:
    print(str(i))
