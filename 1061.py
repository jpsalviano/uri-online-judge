# Event Time - 1061

data = []
for i in range(4):
    data.append(input())
iDay = [int(s) for s in data[0].split() if s.isdigit()][0]
iHour, iMin, iSec = [int(s) for s in data[1].split() if s.isdigit()]
fDay = [int(s) for s in data[2].split() if s.isdigit()][0]
fHour, fMin, fSec = [int(s) for s in data[3].split() if s.isdigit()]

if (iDay == fDay):
    days = 0
    seconds = ((60 - iSec) + fSec) + (((60 - iMin) + fMin)*60) + (((fHour - iHour)*3600)
    hours = seconds / 3600
    #minutes = 
