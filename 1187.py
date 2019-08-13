# 1187

O = input()
M = []

for i in range(144):
    M.append(float(input()))

D = []

for l in range(5):
    for c in range(1+l, 11-l):
        D.append(M[l*12+c])

if O == 'S':
    print('{:.1f}'.format(sum(D)))
else:
    print('{:.1f}'.format(sum(D)/len(D))
