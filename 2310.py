n = int(input())
st, bt, at = 0, 0, 0
s, b, a = 0, 0, 0

for _ in range(n):
    j = input()
    jst, jbt, jat = [int(x) for x in input().split()]
    js, jb, ja = [int(x) for x in input().split()]
    st += jst
    bt += jbt
    at += jat
    s += js
    b += jb
    a += ja
    
print('Pontos de Saque: {:.2f} %.\nPontos de Bloqueio: {:.2f} %.\nPontos de Ataque: {:.2f} %.'.format(100*s/st, 100*b/bt, 100*a/at))
