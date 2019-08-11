# 1184

O = input()
M = []

for i in range(144):
    M.append(float(input()))

D = []

for c in range(12):
    for l in range(c+1, 12):
        D.append(M[l*12+c])

if O == 'S':
    print('{:.1f}'.format(sum(D)))
else:
    print('{:.1f}'.format(sum(D)/len(D)))
