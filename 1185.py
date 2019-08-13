# 1185

O = input()
M = []

for i in range(144):
    M.append(float(input()))

D = []

for l in range(11):
    for c in range(11-l):
        D.append(M[l*12+c])

if O == 'S':
    print('{:.1f}'.format(sum(D)))
else:
    print('{:.1f}'.format(sum(D)/len(D)))

c: 0 ... 10
l: 0 ... 10

l = 10
c = 0
M[120]
