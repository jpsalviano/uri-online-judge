pi = 3.14159

R = float(input())                  #if int() was used instead of float(), python wouldn't support a float as input

def area(r):
  A = pi * (r**2)
  print('A={:0.4f}'.format(A))

area(R)

'''
The format specifier inside the curly braces follows the Python format string syntax. Specifically, in this case, it consists of the following parts:

The empty string before the colon means "take the next provided argument to format()" – in this case the A as the only argument.
The 0.4f part after the colon is the format specification.
The f denotes fixed-point notation.
The 0 is the total width of the field being printed, lefted-padded by spaces.
The 4 is the number of digits after the decimal point.
'''

