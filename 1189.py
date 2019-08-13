# 1188

O = input()
M = []

for i in range(144):
    M.append(float(input()))

D = []

for l in range(7, 12):
    for c in range(12-l, l):
        D.append(M[l*12+c])

if O == 'S':
    print('{:.1f}'.format(sum(D)))
else:
    print('{:.1f}'.format(sum(D)/len(D)))
