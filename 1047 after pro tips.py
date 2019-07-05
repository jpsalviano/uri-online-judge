# Game Time with imnutes - 1047

ih, im, fh, fm = map(int, input().split()) # more pythonic though more verbose:
                                             # [int(i) for i in input().split()] - why []?


if (ih == fh):
    if (im == fm):
        h = 24
        m = 0
    if (im < fm):
        h = 0
        m = fm - im
    if (im > fm):
        h = 23
        m = 60-(im-fm)

if (ih < fh):
    h = fh - ih
    h = h-1 if (im > fm) else h
    m = 60-(im-fm) if (im > fm) else fm-im
        
if (ih > fh):
    h = 24 - ih + fh
    h = - 1 if (im != fm) else h
    m = 0 if (im == fm) else 60-(im-fm)
   
print('O JOGO DUROU ' + str(h) + ' HORA(S) E ' + str(m) + ' MINUTO(S)')
