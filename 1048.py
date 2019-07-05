# Game Time with imnutes - 1047

ih, im, fh, fm = [int(i) for i in input().split()]


if (ih == fh):
    if (im == fm):  # 24 horas - maximo
        h = 24
        m = 0
    if (im < fm):   # 0 hora
        h = 0
        m = fm - im # 23 horas
    if (im > fm):
        h = 23
        m = 60-(im-fm)

if (ih < fh):       # jogatina dentro do mesmo dia
    h = fh - ih
    if (im == fm):  # 08:08 - 09:08 | 01:09 - 23:09
        m = 0
    if (im > fm):   # 08:03 - 09:02 | 08:53 - 10:00
        h -= 1
        m = 60-(im-fm)
    if (im < fm):   # 08:03 - 09:04 | 08:00 - 10:59
        m = fm-im
        
if (ih > fh):       # jogatina passa pela meia noite
    h = 24 - ih + fh
    if (im == fm):  # 23:03 - 01:03 | 14:52 - 10:52
        m = 0
    if (im > fm):   # 23:04 - 01:03 | 14:52 - 10:15
        h -= 1
        m = 60-(im-fm)
    if (im < fm):   # 23:03 - 01:04 | 14:15 - 10:52
        h -= 1
        m = 60-(fm-im)
   
print('O JOGO DUROU ' + str(h) + ' HORA(S) E ' + str(m) + ' MINUTO(S)')
