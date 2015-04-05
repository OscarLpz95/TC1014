#Oscar Lopez
def pal(x):
	x2 = str(x)
	x3 = x2[::-1]
	x4 = int(x3)
	if(x==x4):
		return True
	else:
		return False
		
nonlycherels = 0
Lycherels = 0
npalindromes = 0
x = int(input("Give me the lower bound of the sequence: "))
y = int(input("Give me the upper bound of the sequence: "))
print("Range of numbers analysed: From", x , " to ", y)
for c in range(x,y+1):
	c3 = pal(c)
	if(c3==False):
		c2 = 0
		p2 = False
		candidate = c
		while(c2<30 and p2==False):
			c2 = c2 + 1
			c6 = str(candidate)
			r = c6[::-1]
			r2 = int(r)
			candidate = candidate + r2
			p2 = pal(candidate)
		if(p2==True):
			nonlycherels = nonlycherels + 1
		if(c2==30 and p2==False):
			Lycherels = Lycherels + 1
	else:
		npalindromes = npalindromes + 1

print("The number of natural palindromes is: ", npalindromes)
print("The number of non-Lycherels is: ", nonlycherels)
print("The number of Lycherel candidates is: ", Lycherels)
