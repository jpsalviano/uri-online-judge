p, j1, j2, r, a = [int(i) for i in input().split()]

def par_ou_impar(p, j1, j2):
    if p == 1: # j1 escolheu par
        return 1 if (j1 + j2) % 2 == 0 else 2
    else:      # j1 escolheu impar
        return 1 if (j1 + j2) % 2 != 0 else 2

def roubo_acusa(r, a):
    if r == a == 0:
        return par_ou_impar(p, j1, j2)
    else:
        if r == a == 1:
            return 2
        else:
            return 1

def main():
    print('Jogador {} ganha!'.format(roubo_acusa(r, a)))

main()
