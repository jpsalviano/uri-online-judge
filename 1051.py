# Taxes - 1051

salary = float(input())
taxes = []

if (salary > 4500):
    tax = 28
    taxes.append(tax * (salary-4500) / 100)
    salary = 4500
if (3000 < salary <= 4500):
    tax = 18
    taxes.append(tax * (salary-3000) / 100)
    salary = 3000
if (2000 < salary <= 3000):
    tax = 8
    taxes.append(tax * (salary-2000) / 100)

print('R$ {:.2f}'.format(sum(taxes))) if len(taxes) != 0 else print('Isento')
