#Oscar Lopez
def babylonian(x):
	c=x
	y=0
	while(y!=c):
		y=c
		c=(x/c+c)/2
	return c

x= int(input("Give me a number: "))
a= babylonian(x)
print(a)
