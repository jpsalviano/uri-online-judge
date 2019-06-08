# Average 3 - 1040 

a, b, c, d = [float(i) for i in input().split()]
wa, wb, wc, wd = 2, 3, 4, 1

average = ((wa*a) + (wb*b) + (wc*c) + (wd*d))/(wa+wb+wc+wd)
average = float('{:3.1f}'.format(average))

print('Media: ' + str(average))

if average >= 7.0:
    print('Aluno aprovado.')
    
elif average < 5.0:
    print('Aluno reprovado.')
    
else:
    print('Aluno em exame.')
    
    examScore = float(input())
    print('Nota do exame: '+ str(examScore))
    
    newAverage = (average + examScore)/2
    newAverage = float('{:3.1f}'.format(newAverage))
    
    if newAverage >= 5.0:
        print('Aluno aprovado.')
    else:
        print('Aluno reprovado.')

    print('Media final: ' + str(newAverage))
