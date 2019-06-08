# Bhaskara's Formula - 1036

# answered in: https://github.com/MayaraMachado/URI---Python-3/blob/master/1036%20-%20F%C3%B3rmula%20de%20Bhaskara

a, b, c = [float(i) for i in input().split()] # map(float, input().split()) -> https://stackoverflow.com/questions/10973766/understanding-the-map-function

delta = ((b**2)-4*a*c)

if( (delta < 0) or a == 0): # parentheses
	print( "Impossivel calcular")
	
elif ( delta == 0 ):
	r1 = (-b + delta **(1/2))/(2*a)
	r2 = r1
	print("R1 = "+ "{:0.5f}".format(r1)) # old -> print("R1 = %.5f" %(r1))
	print("R2 = "+ "{:0.5f}".format(r2)) # old-> print("R2 = %.5f" %(r2))

else:
	r1 = (-b + delta **(1/2))/(2*a)
	r2 = (-b - delta **(1/2))/(2*a)
	print("R1 = "+ "{:0.5f}".format(r1))
	print("R2 = "+ "{:0.5f}".format(r2))
