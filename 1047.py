# Game Time with Minutes - 1047

initialHour, initialMinute, finalHour, finalMinute = [int(i) for i in input().split()]

if initialHour == finalHour:
    if initialMinute == finalMinute:
        hour = 24
        minute = 0
    elif initialMinute < finalMinute: # 00:40 / 00:50
        hour = 0
        minute = finalMinute - initialMinute
    elif initialMinute > finalMinute: # 00:55 / 00:10
        hour = 23
        minute = 60 - (initialMinute - finalMinute)

if initialHour < finalHour: # 01:00 / 02:00
    if (finalHour - initialHour) == 1
        hour = 0
        minute = abs()
    if initialMinute == finalMinute:
        minute = 0
    elif initialMinute < finalMinute: # 01:00 / 02:01
        minute = finalMinute - initialMinute
    elif initialMinute > finalMinute: # 01:10 / 02:00
        minute = 60 - (initialMinute - finalMinute)
   
print('O JOGO DUROU ' + str(hour) + ' HORA(S) E ' + str(minute) + ' MINUTO(S)')
