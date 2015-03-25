def find_threes(numbers):
	c=0
	sum=0
	while(c<len(numbers)):
		r=numbers[c]
		c=c+1
		d=r/3
		f=int(d)
		if(d==f):
			sum = sum+r
	return sum
a= find_threes([0,4,2,6,9,8,3,12])
print(a)
