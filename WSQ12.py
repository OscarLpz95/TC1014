def gcd(x,y):
	while(x!=y):
		if(x>y):
			while(x>y):
				x = x-y
				r = x
				return r
		if(x<y):
			while(x<y):
				y = y - x
				b = y
			return b
	if(x==y):
		return x
	
x = int(input("Give me a number: "))
y = int(input("Give me another number: "))
a = gcd(x,y)
print("The GCD to those numbers is: ", a)
