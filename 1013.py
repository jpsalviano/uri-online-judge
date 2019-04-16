# 1013 - The Greatest

'''
Make a program that reads 3 integer values and present the greatest one followed by the message "eh o maior". Use the following formula:



Input
The input file contains 3 integer values.

Output
Print the greatest of these three values followed by a space and the message “eh o maior”.
'''

ABC = input().split()
A = int(ABC[0])
B = int(ABC[1])
C = int(ABC[2])

def theGreatest(A, B, C):
    if A >= B and A >= C:
        greatest = A
    elif B >= A and B >= C:
        greatest = B
    else:
        greatest = C
    print(str(greatest) +' eh o maior')

theGreatest(A, B, C)
